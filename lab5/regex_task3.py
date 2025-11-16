import re
import csv
from utils import load_text

def solve_task3(path: str, output: str):
    text = load_text(path)

    sites = re.findall(r'https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._/-]*)?', text)
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    emails = re.findall(r'[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}', text)
    surnames = re.findall(r'\b[A-Z][a-z]+\b', text)

    # Формируем финальную таблицу
    rows = [["ID", "Surname", "Date", "Email", "Site"]]
    for i, (s, d, e, w) in enumerate(zip(surnames, dates, emails, sites), start=1):
        rows.append([i, s, d, e, w])

    # Сохранение CSV
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(rows)
