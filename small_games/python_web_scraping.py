import requests
from bs4 import BeautifulSoup

req = requests.get('https://quotes.toscrape.com/tag/books/')
soup = BeautifulSoup(req.text, 'lxml')


# grab title
title = soup.select('title')[0].getText()
print(title)

# grab all 10 tag items
tag_items = []

for tag_item in soup.select(".tags-box a.tag"):
    tag_items.append(tag_item.getText().lstrip())
print(tag_items)

books_web_page_url = "https://quotes.toscrape.com/tag/books/page/{}/"

page_no = 1
while True:
    res = requests.get(books_web_page_url.format(page_no)) 
    soup = BeautifulSoup(res.text, 'lxml')

    if "No quotes found!" in soup.select('body')[0].getText():
        break

    for i in range(len(soup.select("span.text"))):
        print(soup.select("span.text")[i].getText())
        print('By ' + soup.select(".author")[i].getText() + '\n')

    page_no += 1