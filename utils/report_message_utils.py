"""
※※※※※※※※※※※※※※※※※※※※※※※※※※※
※   UserName  :   Y.cao ☆彡             
※   FileName  :   report_message
※   Project   ：  北梦测-WMS仓管系统
※   Time      :   2024/5/13 -- 22:14     
※※※※※※※※※※※※※※※※※※※※※※※※※※※
"""
import json
import requests


def ding():
    # 钉钉自定义应用的相关配置
    access_token = '机器人生成的token'
    agent_id = 'YOUR_DINGTALK_AGENT_ID'

    # 消息结构体
    message = {
        "msgtype": "text",
        "text": {
            "content": "http://127.0.0.1:8848/job/wms-test/13/allure/"
        }
    }
    # 发送消息的API地址
    url = f"https://oapi.dingtalk.com/cgi-bin/webhook/send?access_token={access_token}"
    # 发送请求
    response = requests.post(url, json.dumps(message))
    # 打印响应结果
    print(response.text)


def wechat():
    # 企微的webhook地址
    webhook_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8d6432ae-e401-45db-ad8a-7158b9935a84'

    # 消息结构体
    message = {
        "msgtype": "text",
        "text": {
            "content": "http://127.0.0.1:8848/job/wms-test/13/allure/"
        }
    }
    # 发送请求
    response = requests.post(webhook_url, json=message)
    # 打印响应结果
    # print(response.text)


print(wechat())
