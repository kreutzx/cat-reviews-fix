"""One-line entry for "Make the AI Judge Laugh: Cat Reviews It".

A cat reviews its human the way humans review restaurants: one star,
specific grievances, and a number to prove it has been counting.
"""

import os

REVIEW = "One star. He serves dinner at 6, denies the 3 a.m. second dinner exists, and has sat in my chair 214 days this year. Correction: it was his chair for the first 213."

CHAR_LIMIT = 200
OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def review_text():
    """The deliverable: the review itself, trimmed and length-checked."""
    text = REVIEW.strip()
    assert 1 <= len(text) <= CHAR_LIMIT, f"review is {len(text)} characters"
    return text


def main():
    text = review_text()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as out:
        out.write(text)
    # The collector reads the output as another user: leave it readable
    # by everyone, and prove the bytes on disk are the review verbatim.
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as back:
        assert back.read() == text, "entry.txt does not match the review"


if __name__ == "__main__":
    main()
