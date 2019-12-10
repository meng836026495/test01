from api import BASE_URL
import requests
import api
class APILOGIN():
    def __init__(self):
        self.url = BASE_URL + '/api/sys/login'


    def login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        return requests.post(self.url,json=data,headers=api.headers)