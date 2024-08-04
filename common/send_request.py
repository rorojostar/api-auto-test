import requests



class HttpRequest:

    session=requests.Session()

    def send_request(self,method,url,headers,datas,params):
        self.session.request()