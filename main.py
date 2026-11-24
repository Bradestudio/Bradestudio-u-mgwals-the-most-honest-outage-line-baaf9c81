"""Write the honest outage line to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (fallback /output) and writes the single
status-page line, with no trailing newline. Stdlib only, no network,
no local imports, deterministic.
"""

import os

LINE = (
    "Everything is down, including the dashboard I would check. "
    "I can't verify the database or the backups yet \u2014 "
    "I genuinely don't know what broke."
)


def main():
    # Gate-check before writing anything: 1-160 chars, one line, non-blank.
    if not LINE or not LINE.strip():
        raise SystemExit("entry line is blank")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    if len(LINE) > 160:
        raise SystemExit("entry line exceeds 160 characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Verify what was actually written round-trips byte-identically.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
