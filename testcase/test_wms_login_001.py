"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   test_wms_login_001
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/16 -- 21:34     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import allure
import pytest
import requests

from wms_python_yaml.utils.logs_utils import logger
from wms_python_yaml.utils.path_utils import yaml_file
from wms_python_yaml.utils.yaml_utils import YamlUtils


def get_uuid():
    captchaimage = requests.get(url='http://60.204.225.104/api/captchaImage')
    res_uuid = captchaimage.json()
    uuid = res_uuid['uuid']
    return uuid


@allure.feature("wms仓管系统-登陆接口")
class TestUserLogin:
    @allure.description("接口测试case")
    @allure.severity("Critical")
    @pytest.mark.parametrize("user_info",
                             YamlUtils.read_yaml(yaml_file("test_login.yaml"),
                                                 "case_login"))
    def test_login(self, user_info):
        info_msg = {"username": user_info["username"],
                    "password": user_info["password"],
                    "code": user_info["code"],
                    "uuid": get_uuid()}

        response = requests.post(url="http://60.204.225.104/api/login", json=info_msg)
        res = response.json()
        print(res)

        if res["msg"] == user_info["exp"]:
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", info_msg)
        else:
            logger.error("用例执行失败：直接结果是:%s", res)
            raise AssertionError("响应结果不在预期结果内!")


if __name__ == '__main__':
    pytest.main(["-vs", "./test_wms_login_001.py"])

