"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   test_wms_customer_adduser_003
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/20 -- 15:20     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import allure
import pytest
import requests

from wms_python_yaml.utils.db_utils import DBUtils
from wms_python_yaml.utils.logs_utils import logger
from wms_python_yaml.utils.path_utils import yaml_file
from wms_python_yaml.utils.token_utils import get_wms_token
from wms_python_yaml.utils.yaml_utils import YamlUtils


@allure.feature("wms仓管系统-新增客户接口")
class TestAdduser:

    @pytest.fixture(autouse=True)
    def conn_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    @allure.description("接口测试用例")
    @allure.severity("Critical")
    @pytest.mark.parametrize("adduser_msg",
                             YamlUtils.read_yaml(yaml_file("test_customer_adduser.yaml"), "case_customer_adduser"))
    def test_customer_adduser(self, adduser_msg,get_token_fixture):
        response = requests.post(url="http://60.204.225.104:9632/wms/customer",
                                 json={"customerNo": adduser_msg["customerNo"],
                                       "customerName": adduser_msg["customerName"],
                                       "address": adduser_msg["address"],
                                       "mobile": adduser_msg["mobile"],
                                       "tel": adduser_msg["tel"],
                                       "customerPerson": adduser_msg["customerPerson"],
                                       "customerLevel": adduser_msg["customerLevel"],
                                       "email": adduser_msg["email"],
                                       "remark": adduser_msg["remark"],
                                       "bankAccount": adduser_msg["bankAccount"]},
                                 headers={"Authorization": get_token_fixture})
        res = response.json()
        print(res)
        if res == adduser_msg["exp"]:
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", adduser_msg)
            self.db.cud("DELETE from wms_customer WHERE customer_no = %s", (adduser_msg["customerNo"],))

        elif isinstance(res, dict) and "code" in res:
            if res["code"] == adduser_msg["exp"]:
                logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", adduser_msg)

        elif res != adduser_msg["exp"]:
            logger.error("用例执行失败：直接结果是:%s", res)
            self.db.cud("DELETE from wms_customer WHERE customer_no = %s", (adduser_msg["customerNo"],))

        else:
            logger.error("用例执行失败：直接结果是:%s", res)
            raise AssertionError("响应结果不在预期结果内!")


if __name__ == '__main__':
    pytest.main(["-vs", "./test_wms_customer_adduser_003.py"])
