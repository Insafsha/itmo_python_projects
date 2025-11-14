import re
import csv
import os

DATA = "data"  # папка с файлами

# ЗАДАНИЕ 1
with open(os.path.join(DATA, 'task1-en.txt'), encoding='utf-8') as file:
    text1 = file.read()

numbers = re.findall(r'\b(0|[1-9]\d*)(?:\.\d+)?\b', text1)
words = re.findall(r'\b\w{6}\b|\b\w{8}\b', text1)

print("Задание 1:")
print("Числа:", numbers)
print("Слова:", words)

# ЗАДАНИЕ 2
with open(os.path.join(DATA, 'task2.html'), encoding='utf-8') as file:
    text2 = file.read()

content = re.findall(r'content="([^"]+)"', text2)

print("\nЗадание 2:")
print("Content:", content)

# ЗАДАНИЕ 3
with open(os.path.join(DATA, 'task3.txt'), encoding='utf-8') as file:
    text3 = file.read()

# site
sites = re.findall(r'https?://[a-zA-Z0-9.-]+/', text3)
text3 = re.sub(r'https?://[a-zA-Z0-9.-]+/', ' ', text3)

# date
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text3)
text3 = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', text3)

# surname
surnames = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', text3)
text3 = re.sub(r'[A-Z][a-z]+(?!\d\d@|@)', ' ', text3)

# email
emails = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', text3)
text3 = re.sub(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{2,}', ' ', text3)

# формируем ID
ids = list(range(1, len(surnames) + 1))

# собираем таблицу
table = [['ID', 'Surname', 'Date', 'Email', 'Site']]
table += list(zip(ids, surnames, dates, emails, sites))

# сохранение
output_file = os.path.join(DATA, "task3_result.csv")

with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(table)

print("\nЗадание 3:")
print(f"CSV сохранён как {output_file}")
