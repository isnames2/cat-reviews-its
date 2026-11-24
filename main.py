# Cat Reviews Its Human — a one-star review, written by the cat.
# One line, 123 characters, under the 200-character limit.
import os
from pathlib import Path

LINE = "One star. He feeds me late, bought a bed the size of a coaster, and then has the nerve to close the door to the room I own."

def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
