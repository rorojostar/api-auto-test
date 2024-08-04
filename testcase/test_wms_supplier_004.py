"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   test_wms_supplier_004
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/21 -- 15:15     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import allure
import pytest
import requests

from utils.db_utils import DBUtils
from utils.logs_utils import logger
from utils.path_utils import yaml_file
from utils.yaml_utils import YamlUtils


@allure.feature("wms仓管系统-修改供应商信息接口")
class TestSupplier:

    @pytest.fixture(autouse=True)
    def conn_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    @allure.severity("Critical")
    @allure.description("修改供应商信息接口的测试用例")
    @pytest.mark.parametrize("supp_msg", YamlUtils.read_yaml(yaml_file("test_supplier.yaml"), "test_supplier"))
    def test_wms_supplier(self, supp_msg,get_token_fixture):
        response = requests.put(
            url="http://60.204.225.104:9632/wms/supplier",
            json={"id": supp_msg['id'],
                  "supplierNo": supp_msg['supplierNo'],
                  "supplierName": supp_msg['supplierName'],
                  "bankName": supp_msg['bankName'],
                  "bankAccount": supp_msg['bankAccount'],
                  "payableAmount": supp_msg['payableAmount'],
                  "address": supp_msg['address'],
                  "mobileNo": supp_msg['mobileNo'],
                  "telNo": supp_msg['telNo'],
                  "contact": supp_msg['contact'],
                  "level": supp_msg['level'],
                  "email": supp_msg['email'],
                  "remark": supp_msg['remark'],
                  "delFlag": supp_msg['delFlag']},
            headers={"Authorization": get_token_fixture})
        res = response.json()
        print(res)
        try:
            assert res == 1
            logger.info("接口响应符合预期，用例执行成功，请求参数是：%s", supp_msg)
            sql = "UPDATE wms_supplier SET supplier_no = %s,supplier_name= %s,bank_name= %s,bank_account= %s,address= %s,mobile_no= %s,tel_no= %s,contact= %s,level= %s,email= %s,remark= %s WHERE id = 56"
            params = (supp_msg["update_supplierNo"],
                      supp_msg["update_supplierName"],
                      supp_msg["update_bankName"],
                      supp_msg["update_bankAccount"],
                      supp_msg["update_address"],
                      supp_msg["update_mobileNo"],
                      supp_msg["update_telNo"],
                      supp_msg["update_contact"],
                      supp_msg["update_level"],
                      supp_msg["update_email"],
                      supp_msg["update_remark"],)
            self.db.cud(sql, params)
        except AssertionError as e:
            logger.error("用例执行失败：直接结果是:%s", res)
            raise e


if __name__ == '__main__':
    pytest.main(["-vs", "./test_wms_supplier_004.py"])

