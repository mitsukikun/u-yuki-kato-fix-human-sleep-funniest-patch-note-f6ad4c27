#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — entry generator (stdlib only)."""
import os

# FINAL line.
LINE = "v2.4.1 \u2014 Fixed: brain no longer schedules all existential dread for 3:00 a.m.; dread now ships in daylight, where it belongs."

def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 160, f"line is {len(line)} chars, must be 1-160"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    try:
        os.makedirs("/output", exist_ok=True)
    except Exception:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
