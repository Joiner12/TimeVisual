# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 10:01:24 2022

@author: W-H
"""

import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests


def CMCC_LOGIN(
    login_url=r'http://10.10.10.3/ac_portal/20220211170716/pc.html?template=20220211170716&tabs=pwd&vlanid=0&url=http://edge.microsoft.com%2fcaptiveportal%2fgenerate_204'
):
    """
    embeded function
    """

    def wait(locator, timeout=3):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    net_status_info = {'status': False, 'detail': "no initialization"}

    target_base_url = login_url
    if requests.get('https://cn.bing.com/?mkt=zh-CN').status_code == 200:
        net_status_info['status'] = True
        net_status_info['detail'] = "start check net succeed"
        return net_status_info
    try:
        # win平台使用edge,Linux平台使用chrome
        # edge
        if sys.platform == 'win32':
            EDGE = {
                "browserName": "MicrosoftEdge",
                "version": "",
                "platform": "WINDOWS",
                "ms:edgeOptions": {
                    'extensions': [],
                    'args': ['--headless']
                }
            }
            browser = webdriver.Edge(
                executable_path=
                r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
                capabilities=EDGE)
        elif sys.platform == 'linux':
            browserOptions = Options()
            browserOptions.add_argument('bina')
            browserOptions.add_argument('headless')
            browser = webdriver.Chrome(executable_path=r"chromdriver.exe",
                                       options=browserOptions)
        else:
            pass
        net_status_info['detail'] = "webdriver initialization succeed"
    except:
        net_status_info['status'] = False
        net_status_info['detail'] = "webdriver initialization failed"
        return net_status_info
    # sign in
    try:
        browser.get(target_base_url)
        # todo:目标网站无相应情况下直接发送请求
        wait((By.ID, "submit_button_1"))
        browser.find_element(By.ID, "submit_button_1")
        browser.find_element(By.ID, "username").clear()
        browser.find_element(By.ID,
                             "username").send_keys(os.getenv('OA_USERNAME'))
        browser.find_element(By.ID, "password1").clear()
        browser.find_element(By.ID,
                             "password1").send_keys(os.getenv('OA_PASSWORD'))
        browser.find_element(By.ID, 'submit_button_1').click()
        # submit_button_1
        net_status_info['detail'] = "login succeed"
    except:
        net_status_info['status'] = False
        net_status_info['detail'] = "login failed"
        return net_status_info
    # 通过执行js来新开一个窗口
    js = 'window.open("https://cn.bing.com/");'
    browser.execute_script(js)

    handles = (browser.window_handles)  # 获取当前窗口句柄集合（列表类型）

    for handle in handles:  # 切换新窗口
        if handle != browser.current_window_handle:
            browser.switch_to.window(handle)
            break
    # 根据网页元素确定是否登录网络成功
    try:
        wait((By.ID, "est_switch"))
        net_status_info['status'] = True
        net_status_info['detail'] = "final check net succeed"
    except:
        net_status_info['status'] = False
        net_status_info['detail'] = "final check net failed"
    browser.close()  # 关闭当前窗口
    browser.switch_to.window(handles[0])
    browser.close()
    return net_status_info


if __name__ == "__main__":
    print(get_net_status())
