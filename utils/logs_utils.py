"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   logs_utils
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/4/16 -- 22:56     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import logging
from utils.path_utils import INFO_FILE, ERROR_FILE

"""
日志：就是为了记录正确或者错误的接口信息
"""


def get_logger():
    # 初始化日志记录器,设置日志记录器的级别
    logger = logging.getLogger()
    logger.setLevel("DEBUG")

    # 创建并配置流处理器
    sh1 = logging.StreamHandler()
    sh1.setLevel("INFO")

    # 创建并配置文件处理器，用于记录INFO级别的日志（文件名，追加模式，编码格式）
    fh1 = logging.FileHandler(filename=INFO_FILE, mode="w", encoding="utf-8")
    fh1.setLevel("INFO")

    # 创建并配置文件处理器，用于记录ERROR级别的日志（文件名，追加模式，编码格式）
    fh2 = logging.FileHandler(filename=ERROR_FILE, mode="w", encoding="utf-8")
    fh2.setLevel("ERROR")

    # 为日志记录添加处理器
    logger.addHandler(sh1)
    logger.addHandler(fh1)
    logger.addHandler(fh2)

    # 设置日志记录内容(时间戳，文件名，行号，日志级别，消息内容)
    fmat = "%(asctime)s - [%(filename)s - %(lineno)d] - %(levelname)s : %(message)s"
    # 生成的日志做格式化
    my_fmat = logging.Formatter(fmat)
    sh1.setFormatter(my_fmat)
    fh1.setFormatter(my_fmat)
    fh2.setFormatter(my_fmat)

    return logger


logger = get_logger()
