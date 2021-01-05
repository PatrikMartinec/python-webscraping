import requests
import requests_cache
from bs4 import BeautifulSoup
import time

requests_cache.install_cache('doucuji', expire_after=180)
requests_cache.clear()

searched_text = 'Záživné doučovanie matematiky, programovania a informatiky v Praze'

for site in range(1, 193):
    print(f'Strana číslo {site}.')
    url = f'https://www.doucuji.eu/hledam-doucovani?p={site}&q=matematika&c=Praha&skype=1'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find_all('div', class_='info')

    for record in range(len(data)):
        div_content = list(data[record].children)[1]
        title = list(div_content.children)[0].get_text()
        if title == searched_text:
            print(f'Zhoda!\nTvoj nadpis sa našiel vo vyhľadávaní na strane {site} v poradí {record}.')
            exit()
    time.sleep(5)
