import requests

def fetch_weather(city: str):
    api_key = "a9d02180fb9b946d96cb3149c3d15fba"
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&units=metric&appid={api_key}&lang=ru"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_data = {
            "Описание погоды": data["weather"][0]["description"],
            "Температура воздуха": f"{data['main']['temp']}°C",
            "Ощущаемая температура": f"{data['main']['feels_like']}°C",
            "Процент влажности": f"{data['main']['humidity']}%",
            "Атмосферное давление": f"{data['main']['pressure']} гПа"
        }

        for name, value in weather_data.items():
            print(f"{name}: {value}")
    else:
        print(f"Ошибка запроса: {response.status_code}")
        print("Ответ сервера:", response.text)


if __name__ == "__main__":
    fetch_weather("Surgut")
