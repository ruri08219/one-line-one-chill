#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt, the file the sealed gate reads.

Draft line (first pass): a sound that stops is scarier than a sound
that keeps going - the attic floor has creaked in a dead husband's
limp for years, and tonight it stops outside the bedroom door.
Revision (second pass, judged against the brief in order): the attic
line is vivid and crafted but its image - footsteps stopping outside
a door - is a familiar one, so it loses on criterion 4 (original).
The voicemail line keeps the concrete scene (a voicemail, the night
she died) and earns a fresher turn: the new message is dated
tomorrow. Last word "tomorrow" lands the blow and the dread keeps
growing after the line ends - she is going to call again.
"""

import os

ENTRY = (
    "The voicemail my mother left the night she died just played again, "
    "and the new message is dated tomorrow."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "entry must be a single sentence"
    assert text == text.strip() and text, "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
