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


# 0) GET - login - https://www.campingshop.pl/panel/auth/login
r = sess.get(LOGIN_WEBSITE, headers=headers)  #  LOGIN_WEBSITE: http://www.campingshop.pl/panel/auth/login


# 1) POST - login - https://www.campingshop.pl/panel/auth/login z staff_username i staff_password
r = sess.post(LOGIN_WEBSITE, data=payload, headers=headers)
r.html.render()  # tu chciałam przekazać send_cookies_session=True ale dostaję TypeError: render() got an unexpected keyword argument 'send_cookies_session'
                 # mimo, ze 'send_cookies_session' jest w doc'sach https://requests.readthedocs.io/projects/requests-html/en/latest/
print(r.cookies.get_dict())  # brak ciasteczek ;( 


# 2) GET - panel - na https://www.campingshop.pl/panel
r = sess.get("https://www.campingshop.pl/panel", headers=headers)

# 3) GET - login - na https://www.campingshop.pl/panel2/login
r = sess.get("https://www.campingshop.pl/panel2/login", headers=headers)

r.html.render()
print(r.cookies.get_dict())  # brak ciasteczek ;(

# Do uzupełnienia
# 5) POST - login_check - na https://www.campingshop.pl/panel2/login_check
# 	    _username, _password 

# print(r.html.text)

r = sess.get("https://www.campingshop.pl/panel")
print(r.cookies.get_dict())

print(r.html.text.find(".ui-jqgrid-sortable"))
print(r.html.text.find("#jqgh_last-orders_opt"))
