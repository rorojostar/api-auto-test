import pytest
import requests


@pytest.fixture(scope='session')
def get_token_fixture():
    captchaimage = requests.get(url='http://60.204.225.104:9632/captchaImage')
    res_uuid = captchaimage.json()
    uuid = res_uuid['uuid']
    url = 'http://60.204.225.104:9632/login'
    response = requests.post(url=url, json={"username": 'admin',
                                            "password": 'e10adc3949ba59abbe56e057f20f883e',
                                            "code": '2',
                                            "uuid": uuid})
    res = response.json()
    print('Bearer ' + res['token'])
    return 'Bearer ' + res['token']


