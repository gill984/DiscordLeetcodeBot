from time import strptime
import requests
from bs4 import BeautifulSoup
import create_title
from datetime import datetime, tzinfo
import pytz

# Return the latest daily leetcode problem title
# I've seen this accidentally return the second to last problem for some reason
def get_latest_problem_title():
    URL_START = 'href='
    URL_END = 'target='
    DATE_START = 'data-value="'
    DATE_END = '(Coordinated Universal Time)'
    URL = "https://leetcode.com/problemset/all/"
    url = ''
    RETRY_MAX = 10
    attempts = 0

    while url == '' and attempts < RETRY_MAX:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="__next")
        pretty = results.prettify()

        for line in pretty.splitlines():
            if "GMT" in line and URL_START in line and URL_END in line:
                # Check if the current date is the date for the problem we found, that's the one we want
                date = line[line.index(DATE_START) + len(DATE_START) : line.index(DATE_END) - 1]
                problem_time = datetime.strptime(date, '%a %b %d %Y %X %Z%z')
                if datetime.now(tz=pytz.UTC).date() == problem_time.date():
                    url = "https://leetcode.com" + line[line.index(URL_START) + len(URL_START) + 1 :line.index(URL_END) - 2]
                    break
        attempts += 1
    
    if (url == ''):
        return None

    dashed_title = create_title.url_to_dashed_title(url)
    full_title = create_title.dashed_to_title(dashed_title)
    return [url, full_title]

if __name__ == '__main__':
    print(get_latest_problem_title())
