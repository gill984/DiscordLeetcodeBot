import requests
from bs4 import BeautifulSoup

TOKEN_START = 'href='
TOKEN_END = 'target'
URL = "https://leetcode.com/problemset/all/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="__next")
pretty = results.prettify()

urls = []
for line in pretty.splitlines():
    if "GMT" in line and "href" in line and "target" in line:
        urls.append("https://leetcode.com" + line[line.index(TOKEN_START) + len(TOKEN_START) + 1 :line.index(TOKEN_END) - 2])
print (urls)

for url in urls:
    page = requests.get(url)
    print(page.content)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", {"data-cy": "question-title"})
    print (results)
