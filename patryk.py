from bs4 import BeautifulSoup
from requests_html import HTMLSession

from secrets import USER, PASSWORD, LOGIN_WEBSITE


sess = HTMLSession()


payload = {
    "staff_username": USER,
    "staff_password": PASSWORD,
    "send": 1
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
}

r = sess.get(LOGIN_WEBSITE)
r.html.render()

r = sess.post(LOGIN_WEBSITE, data=payload, headers=headers)

for h in r.history:
    print(h.text)
print(r.html.links)
print(r.status_code)

# print(r.html.find("#orders"))
# print(r.html.find("#orders"))
# test = soup.find("div", class_="orders")
