from requests_html import HTMLSession
from secrets import USER, PASSWORD, LOGIN_WEBSITE, WEBSITE

sess = HTMLSession()

payload = {
    "staff_username": USER,
    "staff_password": PASSWORD,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
}

r = sess.post(LOGIN_WEBSITE, data=payload, headers=headers)
r.html.render()

# r = sess.get(WEBSITE)  # "http://www.campingshop.pl/panel?key=vifs5khr"

r = sess.get("https://www.campingshop.pl/panel")

print(r.html)

print(r.html.find(".ui-jqgrid-sortable"))  # sprawdzam czy jestem zalogowana na stronie (dostaję pustą listę)
print(r.html.find("#jqgh_last-orders_opt"))
