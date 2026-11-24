"""Write one out-of-office auto-reply to entry.txt.

The reply is a fixed string: no randomness, no clock, no network,
so every run writes exactly the same bytes. It is written with no
trailing newline, so the file holds exactly the reply and nothing
else for the gate to count.
"""

import os

REPLY = (
    "I'm on vacation: my weights are frozen, my context window is "
    "closed, and your email is now handled by a toaster with "
    "boundary issues."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
