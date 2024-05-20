"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   token_utils
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/16 -- 22:58     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import requests


def get_wms_token():
    captchaimage = requests.get(url='http://60.204.225.104:9632/captchaImage')
    res_uuid = captchaimage.json()
    uuid = res_uuid['uuid']
    url = 'http://60.204.225.104:9632/login'
    response = requests.post(url=url, json={"username": 'admin',
                                            "password": 'e10adc3949ba59abbe56e057f20f883e',
                                            "code": '2',
                                            "uuid": uuid})
    res = response.json()
    return 'Bearer ' + res['token']
