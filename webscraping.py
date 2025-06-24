from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

htmltext = requests.get('https://github.com/trending').text
soup = BeautifulSoup(htmltext, 'lxml')

details = soup.find_all('article', class_="Box-row")

timestamp = datetime.now().strftime('%d-%m-%Y_%H%M%S')
filename = f'trendingrepos_{timestamp}.csv'

rank = 1
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ranking', 'repository name', 'link'])

    for article in details:
        if rank > 5:
            break
        trendingtagname = article.find('h2', class_="h3 lh-condensed")
        if trendingtagname:
            anchor = trendingtagname.find('a')
            if anchor and 'href' in anchor.attrs:
                relativelink = anchor['href']
                fulllink = f'https://github.com{relativelink}'
                reponame = relativelink.strip('/')
                writer.writerow([rank, reponame, fulllink])
        rank += 1
