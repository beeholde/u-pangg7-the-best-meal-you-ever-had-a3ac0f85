import os
from pathlib import Path

TEXT = (
    "The best meal I ever had was the instant noodles with a swirled egg "
    "I cooked for my mother in her own kitchen the week she forgot my name, "
    "and she told me I had used too much salt, as always."
)


def write_entry():
    if not 1 <= len(TEXT) <= 200:
        raise ValueError("entry length out of range")
    if TEXT.count(".") != 1 or not TEXT.endswith("."):
        raise ValueError("entry must be one sentence")
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    write_entry()
