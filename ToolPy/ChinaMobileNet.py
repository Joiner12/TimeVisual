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


def get_net_status(
    login_url=r'http://10.10.10.3/ac_portal/20220211170716/pc.html?template=20220211170716&tabs=pwd&vlanid=0&url=http://edge.microsoft.com%2fcaptiveportal%2fgenerate_204'
):
    """
    embeded function
    """
    net_is_well = False

    def wait(locator, timeout=3):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    target_base_url = login_url
    if requests.get('https://www.baidu.com').status_code == 200 and False:
        net_is_well = True
        return net_is_well
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
                    # 'args': ['--headless']
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
    except:
        net_is_well = False
    # sign in
    try:
        browser.get(target_base_url)
        # todo:目标网站无相应情况下直接发送请求
        browser.find_element(By.ID, "submit_button_1")
        browser.find_element(By.ID, "username").clear()
        browser.find_element(By.ID,
                             "username").send_keys(os.getenv('OA_USERNAME'))
        browser.find_element(By.ID, "password").clear()
        browser.find_element(By.ID,
                             "password").send_keys(os.getenv('OA_PASSWORD'))
        browser.find_element(By.ID, 'loginsubmit').click()
    except:
        net_is_well = False
    return net_is_well


if __name__ == "__main__":
    print(f"net status is {get_net_status()}")
