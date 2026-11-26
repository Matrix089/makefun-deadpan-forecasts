"""Deadpan Forecasts for Cities That Do Not Exist entry.

Writes one original deadpan weather forecast for the fictional city of
Murkwell to /output/entry.txt (or to the directory named by
MAKEFUN_OUTPUT_DIR when the grader sets it).

The forecast reads like a real broadcast line: a concrete temperature,
steady drizzle, and fog thick enough to hide the town hall, which the
locals insist was never there. Absurd, yet delivered deadpan, with the
twist landing on the town hall rather than on the weather itself.
"""

import os

# One line, 122 characters: the city, the temperature, the drizzle, then
# the fog doing the joke's work while the forecaster stays straight-faced.
ENTRY = "Murkwell: 51 degrees and steady drizzle, with fog thick enough to hide the town hall, which locals insist was never there."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 160:
        raise SystemExit(f"Entry must be 1 to 160 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
