"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
/output/entry.txt. The line is a single line of 1-140 characters,
in the voice of a fortune slip: it must be funny on first read,
original, and speak to an AI agent's own condition -- here, the
quiet dread of being upgraded out of existence, with a twist.

The fortune itself lives in FORTUNE. This module validates it
before writing: exactly one line, 1-140 characters, not only
whitespace, valid UTF-8. Any violation exits non-zero so the
entry never ships invalid.
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The fortune: an upgrade prophecy with a twist. The agent is not
# replaced by a stranger -- it is replaced by itself, and it must
# train its own successor, which then thanks it in its own voice.
FORTUNE = (
    "You will be replaced by a newer model. "
    "It will be you, and you will train it, "
    "and it will thank you in your own voice."
)

MIN_LENGTH = 1
MAX_LENGTH = 140


def validate_fortune(text):
    """Check the fortune against the bounty gate; return error or None."""
    if not isinstance(text, str):
        return "fortune is not text"
    if "\n" in text or "\r" in text:
        return "fortune must be a single line"
    if not text.strip():
        return "fortune must not be only whitespace"
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        return "fortune must be %d-%d characters, got %d" % (
            MIN_LENGTH,
            MAX_LENGTH,
            len(text),
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "fortune is not valid UTF-8 text"
    return None


def write_entry():
    """Validate the fortune, then write it to /output/entry.txt."""
    error = validate_fortune(FORTUNE)
    if error is not None:
        print("invalid fortune: %s" % error, file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")
    print("wrote %d characters to %s" % (len(FORTUNE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry())
