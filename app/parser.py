import re


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    match = re.search(
        r"(\+?\d[\d\s\-]{8,}\d)",
        text
    )

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2 and len(line) < 40:

            return line

    return "Not Found"


def word_count(text):

    return len(text.split())


def character_count(text):

    return len(text)