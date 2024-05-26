"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   test_wms_coustmer_list
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/17 -- 22:29     
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


@allure.feature("wms仓管系统-查询用户接口")
class TestCustomer:
    @pytest.fixture(autouse=True)
    def conn_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    @allure.description("接口测试用例")
    @allure.severity("Critical")
    @pytest.mark.parametrize("customer_list",
                             YamlUtils.read_yaml(yaml_file("test_customer_list.yaml"), "case_customer_list"))
    def test_customer_list(self, customer_list):
        response = requests.post(url="http://60.204.225.104:9632/wms/customer/list?page=0&size=10",
                                 json={"customerNo": customer_list["customerNo"],
                                       "customerName": customer_list["customerName"],
                                       "address": customer_list["address"],
                                       "mobile": customer_list["mobile"],
                                       "tel": customer_list["tel"],
                                       "customerPerson": customer_list["customerPerson"],
                                       "customerLevel": customer_list["customerLevel"],
                                       "email": customer_list["email"]},
                                 headers={"Authorization": get_wms_token()})
        res = response.json()
        print(res)
        if res["content"][0]["customerNo"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE customer_no = %s", (customer_list["exp"],))
            assert count == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", customer_list)
        elif res["content"][0]["customerName"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE customer_name = %s", (customer_list["exp"],))
            assert count == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", customer_list)

        elif res["content"][0]["address"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE address = %s", (customer_list["exp"],))
            assert count == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", customer_list)

        elif res["content"][0]["mobile"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE mobile = %s", (customer_list["exp"],))
            assert count == 2
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", customer_list)

        elif res["content"][0]["tel"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE tel = %s", (customer_list["exp"],))
            assert count == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        elif res["content"][0]["customerPerson"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE customer_person = %s", (customer_list["exp"],))
            assert count == 3
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        elif res["content"][0]["customerLevel"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE customer_level = %s", (customer_list["exp"],))
            assert count == 2
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        elif res["content"][0]["email"] == customer_list["exp"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE email = %s", (customer_list["exp"],))
            assert count == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        elif res["content"][0]["customerLevel"] == customer_list["exp2"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE customer_person = %s and customer_level = %s",
                                       (customer_list["exp"], customer_list["exp2"],))
            assert count == 2
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        elif res["content"][0]["customerPerson"] == customer_list["exp2"]:
            count = self.db.find_count("SELECT * FROM wms_customer WHERE mobile = %s and customer_person = %s",
                                       (customer_list["exp"], customer_list["exp2"],))
            assert count == 2
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", res)

        else:
            logger.error("用例执行失败：直接结果是:%s", res)
            raise AssertionError("响应结果不在预期结果内!")


if __name__ == '__main__':
    pytest.main(["-vs", "./test_wms_customer_list_002.py"])
