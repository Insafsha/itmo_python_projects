import re
from utils import load_text, save_text

def solve_task1(path: str, output: str):
    text = load_text(path)

    # Вариант 5:
    # все числа (целые и дробные)
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', text)

    # слова из 6 букв
    words6 = re.findall(r'\b[A-Za-zА-Яа-я]{6}\b', text)

    # слова из 8 букв
    words8 = re.findall(r'\b[A-Za-zА-Яа-я]{8}\b', text)

    result = [
        "Числа:",
        "\n".join(numbers),
        "",
        "Слова из 6 букв:",
        "\n".join(words6),
        "",
        "Слова из 8 букв:",
        "\n".join(words8),
    ]

    save_text(output, "\n".join(result))
