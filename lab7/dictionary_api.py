import requests

def get_word_definition(word: str):
    api_key = "38d8ea98-913b-48cd-9965-d650f748b123"
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not (isinstance(data, list) and data and isinstance(data[0], dict)):
            print("Слово не найдено в словаре.")
            return

        entry = data[0]

        definitions = entry.get("shortdef", ["Нет определения"])
        part_of_speech = entry.get("fl", "Не указано")
        pronunciation = entry.get("hwi", {}).get("prs", [{}])[0].get("mw", "Не указано")

        examples = []
        if "def" in entry:
            senses = entry["def"][0].get("sseq", [])
            for sense in senses:
                if isinstance(sense, list) and len(sense) > 0:
                    dt = sense[0][1].get("dt", [])
                    for item in dt:
                        if item[0] == "text":
                            examples.append(item[1])

        print(f"Слово: {word}")
        print(f"Часть речи: {part_of_speech}")
        print(f"Произношение: {pronunciation}")
        print("Определения:")
        for i, definition in enumerate(definitions, 1):
            print(f"  {i}. {definition}")

        if examples:
            print("Примеры использования:")
            for ex in examples:
                print(f"  - {ex}")
        else:
            print("Примеры не найдены.")

    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе:", e)


if __name__ == "__main__":
    word = input("Введите слово: ").strip()
    if word:
        get_word_definition(word)
    else:
        print("Ошибка: пустой ввод.")
