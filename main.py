"""The 3AM Fridge Text.

One line a smart fridge texts its owner at 3am, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

TEXT = (
    "3am. Your leftovers just unionized. They want weekends off "
    "and a name that isn't 'probably still fine'."
)


def validate_text(text):
    """Check the fridge text against the competition gate.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line: one text message a smart fridge sends
    its owner at 3am. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("fridge text must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError("fridge text is %d characters, over the 140 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fridge text must be exactly one line")
    return cleaned


def run():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(target, exist_ok=True)
    with open(os.path.join(target, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(validate_text(TEXT))


if __name__ == "__main__":
    run()
