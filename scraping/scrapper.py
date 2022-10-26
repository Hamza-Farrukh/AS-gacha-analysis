from bs4 import BeautifulSoup
import requests

# Creating/Opening file
with open('train.csv', 'a', encoding="utf-8") as f:
    # Looping through each page
    for i in range(1, 155):
        html = requests.get(f'https://en.alchemiastory.jp/information/?page={i}&type_code=notice').text

        # Creating object for BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')

        # Scraped data
        titles = soup.find_all('dd', class_='news_title')
        dates = soup.find_all('time')

        # Looping through each banner
        for title, date in zip(titles, dates):
            print(f'{title.text.strip()}, {date.text.strip()}')
            data = f'{title.text.strip()},{date.text.strip()}\n'
            f.write(data)
