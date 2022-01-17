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


def testWebdriver():
    #      _               _       __              _              _         _ _     _
    #  ___| |__   ___  ___| | __  / _| ___  _ __  | |_ ___     __| | ___   | (_)___| |_
    # / __| '_ \ / _ \/ __| |/ / | |_ / _ \| '__| | __/ _ \   / _` |/ _ \  | | / __| __|
    #| (__| | | |  __/ (__|   <  |  _| (_) | |    | || (_) | | (_| | (_) | | | \__ \ |_
    # \___|_| |_|\___|\___|_|\_\ |_|  \___/|_|     \__\___/   \__,_|\___/  |_|_|___/\__|

    print(
        r"      _               _       __              _              _         _ _     _   "
    )
    print(
        r"  ___| |__   ___  ___| | __  / _| ___  _ __  | |_ ___     __| | ___   | (_)___| |_"
    )
    print(
        r" / __| '_ \ / _ \/ __| |/ / | |_ / _ \| '__| | __/ _ \   / _` |/ _ \  | | / __| __|"
    )
    print(
        r"| (__| | | |  __/ (__|   <  |  _| (_) | |    | || (_) | | (_| | (_) | | | \__ \ |_"
    )
    print(
        r" \___|_| |_|\___|\___|_|\_\ |_|  \___/|_|     \__\___/   \__,_|\___/  |_|_|___/\__|"
    )
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    TargetBaseUrl = r'http://172.18.0.28:8080/cas/login?service=http://172.18.0.29/cas#/portal/index'
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
    browser.find_element_by_id(longInButtonId)
    browser.find_element_by_id("username").clear()
    browser.find_element_by_id("username").send_keys('wuhao3')
    browser.find_element_by_id("password").clear()
    browser.find_element_by_id("password").send_keys('chinamobile1_1')
    browser.find_element_by_id(longInButtonId).click()
    # for k in range(10):
    #     browser = click_upcoming_item(browser)
    while True:
        try:
            browser = click_upcoming_item(browser)
        except:
            break
    print(r"                       _         ")
    print(r"   ___ _ __ ___  _ __ | |_ _   _ ")
    print(r"  / _ \ '_ ` _ \| '_ \| __| | | |")
    print(r" |  __/ | | | | | |_) | |_| |_| |")
    print(r"  \___|_| |_| |_| .__/ \__|\__, |")
    print(r"                |_|        |___/ ")
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
        r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a'
    ))
    elementUpcoming = browser.find_element_by_xpath(
        r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a'
    )
    print(elementUpcoming.text)
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
    # for k in range(0, 20):
    testWebdriver()
