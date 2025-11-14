from text_analysis import (
    count_long_titles,
    search_by_author,
    load_books,
    generate_bibliography,
    save_bibliography,
    top20_by_downloads,
    unique_publishers
)

from xml_utils import parse_currency


DATA = "lab2/data/books-en.csv"
CURRENCY = "lab2/data/currency.xml"


if __name__ == "__main__":

    print("1) Длинные названия:")
    print(count_long_titles(DATA))

    print("\n2) Поиск автора:")
    name = input("Введите имя автора: ")
    print(search_by_author(DATA, name))

    print("\n3) Генератор библиографии:")
    books = load_books(DATA)
    bib = generate_bibliography(books)
    save_bibliography(bib)
    print("Сохранено в lab2/results/bibliographic.txt")

    print("\n4) XML currency parse:")
    chars, values = parse_currency(CURRENCY)
    print(chars)
    print(values)

    print("\n5) Издательства:")
    print(unique_publishers(DATA))

    print("\n6) Топ-20 по загрузкам:")
    for title, d in top20_by_downloads(DATA):
        print(title, d)
