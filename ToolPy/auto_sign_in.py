# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:43:05 2022

@author: W-H
"""

import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import datetime
from random import randint, random
import re
import time


def log_in_main_page():
    print(r" __________________________________________________________")
    print(r"|   ____ _                       _           _             |")
    print(r"|  / ___| |__   ___  _ __   __ _| |__  _   _| |_   _  ___  |")
    print(r"| | |   | '_ \ / _ \| '_ \ / _` | '_ \| | | | | | | |/ _ \ |")
    print(r"| | |___| | | | (_) | | | | (_| | |_) | |_| | | |_| | (_) ||")
    print(r"|  \____|_| |_|\___/|_| |_|\__, |_.__/ \__,_|_|\__,_|\___/ |")
    print(r"|                          |___/                           |")
    print(r"|__________________________________________________________|")
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
            # 'args': ['--headless']
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
        browser.find_element_by_xpath(
            r'/html/body/div[5]/div[2]/div[1]/div[1]/a').click()
        wait((
            By.XPATH,
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
        ),
             timeout=10)
        if False:
            filling_words = datetime.now().strftime('%Y-%m-%d')
        else:
            filling_words = piece_lrc()
        browser.find_element_by_xpath(
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
        ).send_keys(filling_words)
        browser.find_element_by_xpath(
            r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/button'
        ).click()
    else:
        print('今日已签到,无需重复签到!')
    # 刷新签到页面
    # 签到信息
    continue_days = 'NaN'
    got_bits = 'NaN'
    time.sleep(2 + random())
    wait((By.XPATH, r'/html/body/div[5]/div[1]/div/a[2]'), timeout=10)
    browser.find_element_by_xpath(r'/html/body/div[5]/div[1]/div/a[2]').click()
    continue_days = browser.find_element_by_xpath(
        r'/html/body/div[5]/div[2]/div[1]/div[2]/ul/li[1]/span[1]').text
    got_bits = browser.find_element_by_xpath(
        r'/html/body/div[5]/div[2]/div[1]/div[2]/ul/li[2]/span').text
    got_bits = re.sub(r'Bit', '', got_bits)
    text_temp = "\t连续签到:%5s天 \t 累计获得:%4s Bit" % (continue_days, got_bits)
    print('—' * 59 + '\n', text_temp.center(40, chr(12288)), '—' * 59)
    browser.quit()


def piece_lrc():
    ret_lrc = ""
    with open(r'./lrc/eason.txt', encoding='utf-8', mode='r') as f:
        all_lines = f.readlines()
        line_cnt = len(all_lines)
        ret_lrc = all_lines[randint(0, line_cnt - 1)]
    ret_lrc = re.sub(r'\[\d{1,}\]:', '', ret_lrc)
    return ret_lrc


if __name__ == "__main__":
    log_in_main_page()
