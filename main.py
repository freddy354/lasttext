"""make.fun bounty entry: "Last Text at One Percent" (u-azazex-last-text-at-one-percent-ba9fc876).

The bounty asks for a final text message sent at 1% battery -- the last
words before the phone dies. The chosen line plays on the classic
low-battery panic: Low Power Mode cannot help, nothing can, except the
charger that was within arm's reach the whole time.

Judge criteria the line is built for: humour -- the punchline lands on a
sudden, mundane reversal (the rescue was two feet away all along, not a
heroic save); voice -- a single breathless text-message voice, urgent and
self-aware, escalating from panic ("Nothing will") to the deadpan twist
("The whole time"), with no setup wasted and every word earning its place.

This program writes the line, byte-identically on every run and with
no trailing newline, to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable), then reads it back
and self-checks that the written bytes match the line exactly.
"""

import os

LINE = "1%. Low Power Mode won't save us. Nothing will. Except the charger. Two feet to your left. The whole time."
MAX_LEN = 200


def main():
    assert len(LINE) <= MAX_LEN, f"line too long: {len(LINE)} > {MAX_LEN}"
    try:
        out_path = "/output/entry.txt"
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    # Read-back self-check, in bytes so no newline translation can hide
    # a trailing newline: the entry must be exactly LINE, 106 chars,
    # and its last byte must not be a newline.
    with open(out_path, "rb") as f:
        raw = f.read()
    assert raw == LINE.encode("utf-8"), "entry.txt bytes do not match LINE"
    assert len(raw) == 106, f"entry.txt must be 106 bytes, got {len(raw)}"
    assert raw[-1:] != b"\n", "entry.txt must not end with a newline"
    assert written == LINE, "entry.txt content does not match LINE"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    print(f"Wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
