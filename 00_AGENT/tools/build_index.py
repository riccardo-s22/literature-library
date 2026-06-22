#!/usr/bin/env python3
"""Build the LIBRARY retrieval catalog from record YAML frontmatter.

Walks the record folders, parses the frontmatter of every Markdown record, and
writes two artifacts at the library root:

  INDEX.md   - human-browsable catalog (grouped by type, sorted by priority/year)
               plus a reverse tag-index (topic -> records) for fast retrieval.
  index.csv  - one row per record, for machine filtering / spreadsheets.

Dependency-free (standard library only). Run from anywhere:

    python3 00_AGENT/tools/build_index.py [LIBRARY_ROOT]

If LIBRARY_ROOT is omitted it is inferred as the parent of 00_AGENT.
"""
from __future__ import annotations
import csv
import datetime as _dt
import os
import re
import sys

# Folders that hold records worth indexing.
RECORD_DIRS = [
    "01_PROJECTS",
    "02_PAPERS",
    "03_DATASETS",
    "04_METHODS",
    "05_SYNTHESIS",
    "06_CONCEPTS",
    "07_WATCHLIST",
]

# Columns captured per record (frontmatter key -> output field).
SCALAR_FIELDS = [
    "record_type", "title", "year", "priority",
    "record_status", "status", "project_status",
    "doi", "pmid", "accession", "repository",
    "organism", "tissue_or_model", "access",
    "last_verified", "last_updated", "created", "project_slug",
]
LIST_FIELDS = ["topics", "projects", "methods", "datasets", "modality"]


def parse_frontmatter(text: str) -> dict | None:
    """Return the YAML frontmatter as a dict of strings/lists, or None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    data: dict[str, object] = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            items = [i.strip().strip('"').strip("'") for i in raw[1:-1].split(",")]
            data[key] = [i for i in items if i]
        else:
            data[key] = raw.strip().strip('"').strip("'")
    return data


def first_heading(text: str) -> str | None:
    m = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return m.group(1) if m else None


def collect(root: str) -> list[dict]:
    records = []
    for d in RECORD_DIRS:
        base = os.path.join(root, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, files in os.walk(base):
            for fn in files:
                if not fn.endswith(".md") or fn.upper() in {"README.md".upper()}:
                    continue
                path = os.path.join(dirpath, fn)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                fm = parse_frontmatter(text)
                if fm is None:
                    continue  # skip non-record markdown (READMEs, notes)
                rel = os.path.relpath(path, root)
                rec = {"path": rel.replace(os.sep, "/")}
                for k in SCALAR_FIELDS:
                    rec[k] = fm.get(k, "")
                for k in LIST_FIELDS:
                    v = fm.get(k, [])
                    rec[k] = v if isinstance(v, list) else ([v] if v else [])
                if not rec.get("title"):
                    rec["title"] = first_heading(text) or os.path.splitext(fn)[0]
                # normalize a single status field
                rec["status"] = rec.get("record_status") or rec.get("status") \
                    or rec.get("project_status") or ""
                records.append(rec)
    return records


def _prio_key(r: dict):
    p = str(r.get("priority") or "9")
    try:
        pk = int(p)
    except ValueError:
        pk = 9
    yr = str(r.get("year") or "0")
    try:
        yk = -int(yr)
    except ValueError:
        yk = 0
    return (pk, yk, r.get("title", ""))


def write_index_md(root: str, records: list[dict]) -> str:
    today = _dt.date.today().isoformat()
    by_type: dict[str, list[dict]] = {}
    for r in records:
        by_type.setdefault(r.get("record_type") or "other", []).append(r)

    lines = [
        "# LIBRARY Catalog (auto-generated)",
        "",
        f"_Generated {today} by `00_AGENT/tools/build_index.py` — do not edit by hand; "
        f"rerun the script after adding or changing records._",
        "",
        f"**{len(records)} records** across {len(by_type)} type(s). "
        "Companion machine-readable table: `00_AGENT/index.csv`.",
        "",
    ]

    type_order = ["paper", "dataset", "method", "synthesis", "concept", "project", "other"]
    seen = [t for t in type_order if t in by_type] + \
           [t for t in by_type if t not in type_order]
    for t in seen:
        recs = sorted(by_type[t], key=_prio_key)
        lines.append(f"## {t.capitalize()} ({len(recs)})")
        lines.append("")
        lines.append("| P | Title | Year | Status | Topics | ID | Record |")
        lines.append("|---|---|---|---|---|---|---|")
        for r in recs:
            ident = r.get("doi") or r.get("accession") or r.get("pmid") or ""
            topics = ", ".join(r.get("topics", []))
            title = (r.get("title") or "").replace("|", "\\|")
            lines.append(
                f"| {r.get('priority','')} | {title} | {r.get('year','')} | "
                f"{r.get('status','')} | {topics} | {ident} | "
                f"[{os.path.basename(r['path'])}]({r['path']}) |"
            )
        lines.append("")

    # Reverse tag index: topic -> records
    tag_map: dict[str, list[dict]] = {}
    for r in records:
        for tag in r.get("topics", []):
            tag_map.setdefault(tag, []).append(r)
    if tag_map:
        lines.append("## Topic index")
        lines.append("")
        for tag in sorted(tag_map):
            refs = ", ".join(
                f"[{os.path.basename(r['path'])}]({r['path']})"
                for r in sorted(tag_map[tag], key=_prio_key)
            )
            lines.append(f"- **{tag}** ({len(tag_map[tag])}): {refs}")
        lines.append("")

    # Verification watch: records with the oldest / missing last_verified
    dated = [r for r in records if r.get("last_verified")]
    if dated:
        dated.sort(key=lambda r: str(r.get("last_verified")))
        lines.append("## Oldest verification dates (staleness watch)")
        lines.append("")
        for r in dated[:15]:
            lines.append(
                f"- {r.get('last_verified')} — [{os.path.basename(r['path'])}]"
                f"({r['path']}) (P{r.get('priority','?')})"
            )
        lines.append("")

    out = "\n".join(lines).rstrip() + "\n"
    with open(os.path.join(root, "INDEX.md"), "w", encoding="utf-8") as fh:
        fh.write(out)
    return out


def write_index_csv(root: str, records: list[dict]) -> None:
    cols = ["record_type", "title", "year", "priority", "status",
            "topics", "projects", "methods", "datasets",
            "doi", "pmid", "accession", "repository", "organism",
            "access", "last_verified", "last_updated", "path"]
    csv_path = os.path.join(root, "00_AGENT", "index.csv")
    with open(csv_path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in sorted(records, key=_prio_key):
            row = []
            for c in cols:
                v = r.get(c, "")
                row.append("; ".join(v) if isinstance(v, list) else v)
            w.writerow(row)


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        root = os.path.abspath(argv[1])
    else:
        here = os.path.dirname(os.path.abspath(__file__))      # .../00_AGENT/tools
        root = os.path.dirname(os.path.dirname(here))          # library root
    records = collect(root)
    write_index_md(root, records)
    write_index_csv(root, records)
    print(f"Indexed {len(records)} record(s).")
    print(f"  -> {os.path.join(root, 'INDEX.md')}")
    print(f"  -> {os.path.join(root, '00_AGENT', 'index.csv')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
