# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:43:05 2022

@author: W-H
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


def log_in_main_page():
    print(r"   ____ _                       _           _")
    print(r"  / ___| |__   ___  _ __   __ _| |__  _   _| |_   _  ___")
    print(r" | |   | '_ \ / _ \| '_ \ / _` | '_ \| | | | | | | |/ _ \ ")
    print(r" | |___| | | | (_) | | | | (_| | |_) | |_| | | |_| | (_) |")
    print(r"  \____|_| |_|\___/|_| |_|\__, |_.__/ \__,_|_|\__,_|\___/")
    print(r"                          |___/")
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    TargetBaseUrl = r'https://www.chongbuluo.com/'
    # edge
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
        executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
        capabilities=EDGE)
    # browser.set_window_size(200, 200)
    browser.get(TargetBaseUrl)
    # log in
    browser.find_element_by_css_selector(r'#welcome > a:nth-child(1)').click()
    # 等待加载
    wait((By.XPATH, r'//*[@id="main_message"]/div/div[1]/h3'))
    browser.find_element_by_name("username").clear()
    browser.find_element_by_name("username").send_keys('Risky_JR')
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys('Risky11#')
    browser.find_element_by_name('loginsubmit').click()
    # 签到页面
    wait((By.XPATH, r'/html/body/div[6]/div[1]/div/div/ul/li[15]/a'),
         timeout=10)
    browser.find_element_by_xpath(
        r'/html/body/div[6]/div[1]/div/div/ul/li[15]/a').click()
    #
    wait((By.XPATH, r'/html/body/div[5]/div[1]/div/a[2]'), timeout=10)
    # 签到
    # /html/body/div[5]/div[2]/div[1]/div[1]/a
    sign_in_text = browser.find_element_by_xpath(
        r'/html/body/div[5]/div[2]/div[1]/div[1]/a').text
    if not '已签到' in sign_in_text:
        print(True)
        browser.find_element_by_xpath(
            r'/html/body/div[5]/div[2]/div[1]/div[1]/a').click()
        wait((
            By.XPATH,
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
        ),
             timeout=10)
        browser.find_element_by_xpath(
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
        ).send_keys(str(time.asctime(time.localtime(time.time()))))
        browser.find_element_by_xpath(
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/button'
        ).click()
    else:
        print('已签到')
    browser.quit()


if __name__ == "__main__":
    log_in_main_page()