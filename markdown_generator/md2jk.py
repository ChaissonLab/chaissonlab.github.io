#!/usr/bin/env python3
"""
Convert a Medline-format file of publications into Jekyll markdown
files for the 'publications' collection.

Usage:
    python medline2jekyll.py pubs.medline
"""

import os
import re
import sys

OUT_DIR = "_publications"


def slugify(s: str) -> str:
    """Turn a title into a URL/filename-friendly slug."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "paper"


def yaml_escape(s: str) -> str:
    """Escape double quotes for YAML."""
    return s.replace('"', '\\"')


def parse_medline_records(lines):
    """Parse Medline records into a list of dicts."""
    records = []
    current = {}
    current_tag = None

    for raw in lines:
        line = raw.rstrip("\n")

        if not line.strip():
            if current:
                records.append(current)
                current = {}
                current_tag = None
            continue

        if line.startswith("      "):
            value = line[6:].strip()
            if current_tag:
                current[current_tag][-1] += " " + value
            continue

        tag = line[:4].strip()
        value = line[6:].strip()

        if tag:
            current_tag = tag
            current.setdefault(tag, []).append(value)

    if current:
        records.append(current)

    return records


def parse_date(dp_values):
    """Parse DP field into YYYY-MM-DD."""
    if not dp_values:
        return "1900-01-01"

    dp = dp_values[0]
    tokens = dp.split()

    year = tokens[0] if tokens else "1900"

    month = 1
    if len(tokens) >= 2:
        m = tokens[1].lower()
        months = {
            "jan": 1, "feb": 2, "mar": 3, "apr": 4,
            "may": 5, "jun": 6, "jul": 7, "aug": 8,
            "sep": 9, "oct": 10, "nov": 11, "dec": 12
        }
        month = months.get(m[:3], 1)

    day = 1
    if len(tokens) >= 3 and tokens[2].isdigit():
        day = int(tokens[2])

    return f"{year}-{month:02d}-{day:02d}"


def extract_doi(aid_values, lid_values):
    """Extract DOI from AID or LID fields."""
    for vals in (aid_values or []):
        parts = vals.split()
        if parts and "doi" in vals.lower():
            if parts[0].lower().startswith("10."):
                return parts[0]

    for vals in (lid_values or []):
        m = re.search(r"(10\.\S+)", vals)
        if m:
            return m.group(1)

    return ""


def format_authors(record):
    """Prefer FAU; fallback to AU."""
    if "FAU" in record:
        return ", ".join(record["FAU"])
    if "AU" in record:
        return ", ".join(record["AU"])
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: python medline2jekyll.py pubs.medline")
        sys.exit(1)

    medline_path = sys.argv[1]
    if not os.path.exists(medline_path):
        print(f"Medline file not found: {medline_path}")
        sys.exit(1)

    with open(medline_path) as f:
        lines = f.readlines()

    records = parse_medline_records(lines)
    print(f"Parsed {len(records)} records.")

    os.makedirs(OUT_DIR, exist_ok=True)

    for rec in records:
        pmid = rec.get("PMID", [""])[0]
        title = rec.get("TI", ["Untitled"])[0].strip("{}")
        journal = rec.get("JT", [""])[0]
        date_str = parse_date(rec.get("DP"))
        authors = format_authors(rec)
        doi = extract_doi(rec.get("AID"), rec.get("LID"))

        if doi:
            link = f"https://doi.org/{doi}"
        elif pmid:
            link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        else:
            link = ""

        safe_title = yaml_escape(title)
        safe_journal = yaml_escape(journal)
        safe_authors = yaml_escape(authors)
        safe_doi = yaml_escape(doi)
        safe_pmid = yaml_escape(pmid)
        safe_link = yaml_escape(link)

        slug = slugify(title[:80])
        filename = f"{date_str}-{slug}.md"
        out_path = os.path.join(OUT_DIR, filename)

        # YAML Front Matter only
        lines_out = []
        lines_out.append("---")
        lines_out.append(f'title: "{safe_title}"')
        lines_out.append("collection: publications")
        lines_out.append(f"date: {date_str}")

        if journal:
            lines_out.append(f'venue: "{safe_journal}"')
        if authors:
            lines_out.append(f'authors: "{safe_authors}"')
        if doi:
            lines_out.append(f'doi: "{safe_doi}"')
        if pmid:
            lines_out.append(f'pmid: "{safe_pmid}"')
        if link:
            lines_out.append(f'link: "{safe_link}"')

        lines_out.append("---")
        lines_out.append("")  # empty body; Jekyll doesn't require content

        with open(out_path, "w") as out_f:
            out_f.write("\n".join(lines_out))

        print(f"Wrote {out_path}")

    print("Done.")


if __name__ == "__main__":
    main()

