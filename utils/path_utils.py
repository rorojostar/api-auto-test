"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   path_utils
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/17 -- 21:46     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import os

"""
路径封住复用性比较高，值得做成方法被多次调用
"""

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def yaml_file(yaml_name):
    yaml_dir = os.path.join(BASE_DIR, "datas")
    yaml_file = os.path.join(yaml_dir, yaml_name)

    return yaml_file


# 封装日志路径
LOGER_DIR = os.path.join(BASE_DIR, "logs")
INFO_FILE = os.path.join(LOGER_DIR, "info_logs")
ERROR_FILE = os.path.join(LOGER_DIR, "error_logs")

# 封装allure路径
REPORT_DIR = os.path.join(BASE_DIR, "report")
REPORT_JSON = os.path.join(REPORT_DIR, "allure_json")
REPORT_HTML = os.path.join(REPORT_DIR, "allure_html")

# 封装case存放路径
CASES_FILE = os.path.join(BASE_DIR, "testcase")
print(CASES_FILE)