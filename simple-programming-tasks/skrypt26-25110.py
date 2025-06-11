#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv
import time

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

    def to_dict(self):
        return {
            "header_name": self.header_name,
            "price": self.price,
            "price_for_m2": self.price_for_m2
        }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

base_url = "https://www.otodom.pl/pl/oferty/sprzedaz/dom/gdynia"
params = {
    "priceMax": "600000",
    "limit": "36",
    "page": 1
}

homes = []

for page in range(1, 4): 
    print(f"Pobieranie strony {page}")
    params["page"] = page
    response = requests.get(base_url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    offers = soup.select("li[data-cy='listing-item']")

    for offer in offers:
        title = offer.select_one("h3").text.strip() if offer.select_one("h3") else "Brak"
        price = offer.select_one("span[data-cy='listing-item-price']").text.strip() if offer.select_one("span[data-cy='listing-item-price']") else "Brak"
        price_m2 = offer.select_one("p:contains('zł/m²')")
        price_m2 = price_m2.text.strip() if price_m2 else "Brak"

        home = Home(title, price, price_m2)
        homes.append(home)

    time.sleep(1)  


with open("home.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["header_name", "price", "price_for_m2"])
    writer.writeheader()
    for home in homes:
        writer.writerow(home.to_dict())

print(f"Zapisano {len(homes)} ofert do 'home.csv'.")
