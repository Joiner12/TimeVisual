# -*- coding:utf-8 -*-
from selenium import webdriver
import os, time
import json


def rewrite_cookies():
    # 1.初始化selenium 驱动
    EDGE = {
        "browserName": "MicrosoftEdge",
        "version": "",
        "platform": "WINDOWS",
        # "ms:edgeOptions": {"extensions": [], "args": ["--headless"]},
        "ms:edgeOptions": {"extensions": []},
    }
    browser = webdriver.Edge(
        executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
        capabilities=EDGE,
    )
    try:
        browser.get("https://www.bilibili.com")
        browser.delete_all_cookies()  # 先删除cookies
        time.sleep(30)  # 用于手动登录账号（利用扫码登录），这是人工操作的
        loginCookies = browser.get_cookies()  # 读取登录之后浏览器的cookies
        jsonCookies = json.dumps(loginCookies)  # 将字典数据转成json数据便于保存

        with open(r"D:\Code\TimeVisual\ToolPy\cookie.json", "w") as f:  # 写进文本保存
            f.write(jsonCookies)
        print("cookies 更新成功")
    except:
        # 关闭浏览器
        browser.close()


if __name__ == "__main__":
    rewrite_cookies()
