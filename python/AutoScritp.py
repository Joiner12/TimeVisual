# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:23:50 2021

@author: W-H
"""

"""
    自动处理公文系统文件
"""




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from numpy import random
def testWebdriver():
    TargetBaseUrl = r'http://172.18.0.28:8080/cas/login?service=http://172.18.0.29/cas#/portal/index'
    # TargetBaseUrl = r"file:///C:/Users/W-H/Desktop/login.htm"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40',
    #     'Cookie': 'portal_2_uid=c9791325-f44e-4a05-a134-1f8e19eab0ce'
    #     # portal_2_uid=c9791325-f44e-4a05-a134-1f8e19eab0ce
    # }

    # 以下ip使用自己可使用的代理IP
    proxy_arr = [
        '--proxy-server=http://171.35.141.103:9999',
        '--proxy-server=http://36.248.132.196:9999',
        # '--proxy-server=http://125.46.0.62:53281',
        '--proxy-server=http://219.239.142.253:3128',
        '--proxy-server=http://119.57.156.90:53281',
        '--proxy-server=http://60.205.132.71:80',
        '--proxy-server=https://139.217.110.76:3128',
        '--proxy-server=https://116.196.85.150:3128'
    ]

    chromeOptions = Options()

    browser = webdriver.Chrome(
        executable_path=r"D:\Code\TimeVisual\python\chromedriver.exe", options=chromeOptions)

    # browser.set_window_size(200, 200)

    browser.get(TargetBaseUrl)
    # check login status
    logInStatus = True
    longInButtonId = "normalLoginButton"
    try:
        browser.find_element_by_id(longInButtonId)
    except:
        print('no such element')
        logInStatus = False

    if logInStatus:
        browser.find_element_by_id("username").clear()
        browser.find_element_by_id("username").send_keys('wuhao3')
        browser.find_element_by_id("password").clear()
        browser.find_element_by_id("password").send_keys('chinamobile1_1')
    browser.find_element_by_id(longInButtonId).click()
    # browser.quit()


if __name__ == "__main__":
    testWebdriver()
