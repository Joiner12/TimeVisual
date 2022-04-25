# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:23:50 2021

@author: W-H
"""
"""
    自动处理公文系统文件
"""

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from numpy import random
import time
import requests
from logger import Logger
import os
# 日志文件
lg = Logger(logging_service='oa')


def testWebdriver():
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    # 检查网络连接状态
    TargetBaseUrl = r'http://172.18.0.28:8080/cas/login?service=http://172.18.0.29/cas#/portal/index'
    if not requests.get(TargetBaseUrl).status_code == 200:
        lg.error("网络连接失败")
        return
    # browserOptions = Options()
    # browserOptions.add_argument('headless')
    # chrome
    # browser = webdriver.Chrome(executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
    #                            options=browserOptions)
    # edge
    EDGE = {
        "browserName": "MicrosoftEdge",
        "version": "",
        "platform": "WINDOWS",

        # 关键是下面这个
        "ms:edgeOptions": {
            'extensions': [],
            'args': [
                '--headless'
                # '--disable-gpu',
                # '--remote-debugging-port=9222',
            ]
        }
    }
    browser = webdriver.Edge(
        executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
        capabilities=EDGE)
    # browser.set_window_size(200, 200)
    browser.get(TargetBaseUrl)
    # login status
    longInButtonId = "normalLoginButton"
    wait((By.ID, longInButtonId))
    browser.find_element(By.ID, longInButtonId)
    browser.find_element(By.ID, "username").clear()
    browser.find_element(By.ID, "username").send_keys(os.getenv('OA_USERNAME'))
    browser.find_element(By.ID, "password").clear()
    browser.find_element(By.ID, "password").send_keys(os.getenv('OA_PASSWORD'))
    browser.find_element(By.ID, longInButtonId).click()
    # for k in range(10):
    #     browser = click_upcoming_item(browser)
    while True:
        try:
            browser = click_upcoming_item(browser)
        except:
            break
    lg.info("empty to do list", "info")
    browser.quit()


def click_upcoming_item(browser, *args, **kwargs):
    """处理待办子功能模块

    参数
    ----------
    browser : webdriver
        浏览器驱动

    返回值
    -------
    browser : webdriver
        浏览器驱动

    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    # scroll for load element js
    browser.execute_script("window.scrollBy(0,3000)")
    wait((
        By.XPATH,
        r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[1]/div/div/div/div[2]/ul/li[1]/div[1]/span[2]'
    ))
    elementUpcoming = browser.find_element_by_xpath(
        r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[1]/div/div/div/div[2]/ul/li[1]/div[1]/span[2]'
    )
    print(elementUpcoming.text)
    lg.info("\r\n" + elementUpcoming.text)
    browser.execute_script("arguments[0].click();", elementUpcoming)
    time.sleep(3 + random.rand())
    all_h = browser.window_handles
    browser.switch_to.window(all_h[1])
    browser.execute_script("window.scrollBy(0,3000)")
    time.sleep(3 + random.rand())
    wait((By.CSS_SELECTOR, '.submit_btn.form_btn1'))
    browser.execute_script(
        "arguments[0].click();",
        browser.find_element_by_css_selector('.submit_btn.form_btn1'))
    time.sleep(1 + random.rand())
    # traceback
    browser.switch_to.window(all_h[0])
    browser.execute_script("window.scrollBy(0,1)")
    return browser


if __name__ == "__main__":
    testWebdriver()