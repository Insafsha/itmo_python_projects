import re
from utils import load_text, save_text

def solve_extra(path: str, output: str):
    text = load_text(path)

    # Всё, что начинается с пробела
    dates = re.findall(r' (?:(\d{4}[-/.]\d{2}[-/.]\d{2}))', text)
    emails = re.findall(r' ([a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,})', text)
    sites = re.findall(r' (https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._/-]*)?)', text)

    result = [
        "Даты:",
        "\n".join(dates),
        "",
        "Emails:",
        "\n".join(emails),
        "",
        "Sites:",
        "\n".join(sites),
    ]

    save_text(output, "\n".join(result))
