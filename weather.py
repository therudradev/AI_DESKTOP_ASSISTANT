import requests
from bs4 import BeautifulSoup


def weather(city: str = "patna") -> str:
    """
    Fetch weather using a simple BeautifulSoup scraper.
    Compatible with all Python installations (no lxml clean dependency).
    """

    city = city.replace(" ", "+")
    url = f"https://www.google.com/search?q=weather+{city}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")

        # Temperature
        temp = soup.find("span", {"id": "wob_tm"})
        # Weather description
        desc = soup.find("span", {"id": "wob_dc"})

        if temp and desc:
            return f"{temp.text} °C, {desc.text}"
        else:
            return "Sorry, I couldn't fetch the weather right now."

    except Exception as e:
        print("Weather error:", e)
        return "Sorry, I couldn't fetch the weather right now."
