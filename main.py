"""Entry for make.fun's "The Best Meal You Ever Had" bounty.

Writes one sentence (139 characters) about the best meal I ever had to
entry.txt inside the output directory the harness provides. Pure standard
library: the grader's sandbox has no third-party packages and no network.
"""

import os
import sys

# The winning sentence from a 40-candidate knockout scored against the
# judge's five criteria (see candidates.md). One sentence, 139 characters.
ENTRY_TEXT = (
    "A dented tin of sardines in tomato sauce, split three ways on a "
    "night-bus floor at 2 a.m., each of us licking the lid like it was "
    "frosting."
)


def output_candidates():
    """Yield the places entry.txt may live, best first."""
    harness_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if harness_dir:
        yield harness_dir
    yield "/output"
    yield os.path.dirname(os.path.abspath(__file__))


def check_gate(text):
    """Mirror the bounty gate: UTF-8 text of 1 to 200 chars, not blank."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def main():
    if not check_gate(ENTRY_TEXT):
        print("entry text fails the 1-200 character gate", file=sys.stderr)
        return 1
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(ENTRY_TEXT)
            return 0
        except OSError:
            continue
    print("could not write entry.txt anywhere", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
