import re
import unicodedata


def clean_text(raw_text: str) -> str:
    if not isinstance(raw_text, str):
        raise TypeError("input must be a string")
    if not raw_text.strip():
        raise ValueError("cannot process empty text")

    text = unicodedata.normalize("NFC", raw_text)

    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    text = " ".join(
        character
        for character in text
        if unicodedata.category(character) != "Cc"
        or character in "\n\t"
    )

    lines = [
        re.sub(r"[^\S\n]+", "", line).strip()
        for line in text.split("\n")
    ]

    text = "\n ".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    text = text.strip()

    if not text:
        raise ValueError("Document contains no usable text")
    return text
