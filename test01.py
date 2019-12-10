import requests
 # 验证码URL
 # http://localhost/index.php?m=Home&c=User&a=verify

# 登录接口url
# http://localhost/index.php?m=Home&c=User&a=do_login
session = requests.Session()
session.get('http://localhost/index.php?m=Home&c=User&a=verify')
# print(r.cookies)
# cookie = {"PHPSESSID":r.cookies["PHPSESSID"]}
# print(cookie)
data = {"username":"17631000488","password":"123456","verify_code":"8888"}
r = session.post('http://localhost/index.php?m=Home&c=User&a=do_login', data=data)
# data = {"username": "17631000488", "password":"123456","verify_code":"8888"}
# url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
# r = requests.post(url=url_login, data=data, cookies=cookie)
# print(r.text)
print(r.text)