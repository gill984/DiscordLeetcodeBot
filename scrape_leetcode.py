import requests
from bs4 import BeautifulSoup
import create_title

# Return the latest daily leetcode problem title
# I've seen this accidentally return the second to last problem for some reason
def get_latest_problem_title():
    TOKEN_START = 'href='
    TOKEN_END = 'target='
    URL = "https://leetcode.com/problemset/all/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    pretty = results.prettify()

    urls = []
    for line in pretty.splitlines():
        if "GMT" in line and TOKEN_START in line and TOKEN_END in line:
            urls.append("https://leetcode.com" + line[line.index(TOKEN_START) + len(TOKEN_START) + 1 :line.index(TOKEN_END) - 2])

    dashed_title = create_title.url_to_dashed_title(urls[-1])
    full_title = create_title.dashed_to_title(dashed_title)
    return [urls[-1], full_title]
