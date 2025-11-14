from csv import reader
import random


def count_long_titles(path, min_len=30):
    count = 0
    with open(path, encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for row in table:
            if len(row[1]) > min_len:
                count += 1
    return count


def search_by_author(path, author_name):
    results = []
    with open(path, encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for row in table:
            if author_name.lower() in row[2].lower():
                results.append(row)
    return results


def load_books(path):
    books = []
    with open(path, encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for index, row in enumerate(table, start=1):
            books.append({
                'index': index,
                'author': row[2],
                'title': row[1],
                'year': row[3],
                'downloads': int(row[5]) if row[5].isdigit() else 0
            })
    return books


def generate_bibliography(books, n=20):
    chosen = random.sample(books, n)
    return [
        f"{b['index']}. {b['author']}. {b['title']} - {b['year']}\n"
        for b in chosen
    ]


def save_bibliography(lines, path="lab2/results/bibliographic.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def top20_by_downloads(path):
    result = []
    with open(path, encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for row in table:
            try:
                downloads = int(row[5])
                result.append((row[1], downloads))
            except:
                pass
    return sorted(result, key=lambda x: x[1], reverse=True)[:20]


def unique_publishers(path):
    pubs = set()
    with open(path, encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)
        for row in table:
            pubs.add(row[4])
    return sorted(pubs)
