import requests
from bs4 import BeautifulSoup
import pprint

URL = "https://rezka.ag/films/historical/"

HEADERS = {
    "Accept": "text/html, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response
def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(
        'div',class_="b-content__inline_item"
    )
    films = []
    for item in items:
        info = item.find("div", class_="b-content__inline_item-link").find("div").getText().split(", ")

        film = {
            "title": item.find("div", class_="b-content__inline_item-link").find("a").getText(),
            "link": item.find("div", class_="b-content__inline_item-link").find("a").get("href"),
            "year": info[0],
            "country": info[1],
            "genre": info[2]
        }
        films.append(film)
    return films
def parsers():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for i in range(1, 10):
         html = get_html(f"{URL}page/{i}/")
         current_page = get_data_from_page(html.text)
         films.extend(current_page)
    else:
        raise Exception("Error in parser")
parsers()

html = get_html(URL)
print(html.text)
get_data_from_page(html.text)