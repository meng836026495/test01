import unittest

from api import headers
from api.api_login import APILOGIN
from tools.assert_common import assert_login


class Test_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_login = APILOGIN()


    def test01_login(self,mobile="13800000002",passsword="123456"):
        r = self.api_login.login(mobile, passsword)
        token =r.json().get("data")
        headers["Authorization"]="Bearer "+token
        assert_login(self,r)
        print(r.json())
        print(headers)
        print(r.status_code)