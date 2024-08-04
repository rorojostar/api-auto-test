# -*- coding: utf-8 -*-
"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   test_run
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/17 -- 22:25     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""

import os
import pytest
from utils.path_utils import REPORT_JSON, REPORT_HTML, CASES_FILE


if __name__ == '__main__':
    pytest.main(["-vs", CASES_FILE, "--alluredir", REPORT_JSON, "--clean-alluredir"])
    os.system("allure generate %s -o %s --clean" % (REPORT_JSON, REPORT_HTML))
