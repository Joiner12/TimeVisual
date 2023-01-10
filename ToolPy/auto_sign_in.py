# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:43:05 2022

@author: W-H
"""

import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import datetime
from random import randint, random
import re
import time
import sys
from ChinaMobileNet import CMCC_LOGIN
from logger import Logger
import os
# workspace
cmd = '''cd D:\Code\TimeVisual\ToolPy '''
os.system(cmd)


def log_in_main_page():
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    chongbuluo_log = Logger()
    TargetBaseUrl = r'https://www.chongbuluo.com/'
    chongbuluo_log.log('开始自动签到，完成配置', level='info')
    cmcc_net = CMCC_LOGIN()
    if not cmcc_net['status']:
        chongbuluo_log.log(cmcc_net['detail'], level='error')
        return
    else:
        chongbuluo_log.log(cmcc_net['detail'], level='info')
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
    except:
        chongbuluo_log.log('浏览器句柄初始化失败', level='error')
        # return
    # browser.set_window_size(200, 200)
    try:
        browser.get(TargetBaseUrl)
        # log in
        browser.find_element(By.CSS_SELECTOR,
                             '#welcome > a:nth-child(1)').click()
        # 等待加载
        wait((By.XPATH, r'//*[@id="main_message"]/div/div[1]/h3'))
        browser.find_element(By.NAME, "username").clear()
        browser.find_element(By.NAME,
                             "username").send_keys(os.getenv('CBL_USERNAME'))
        browser.find_element(By.NAME, "password").clear()
        browser.find_element(By.NAME,
                             "password").send_keys(os.getenv('CBL_PASSWORD'))
        browser.find_element(By.NAME, 'loginsubmit').click()
    except:
        chongbuluo_log.log('输入账号密码失败', level='error')
        return
    # 签到页面
    try:
        wait((By.XPATH, r'/html/body/div[6]/div[1]/div/div/ul/li[15]/a'),
             timeout=10)
        browser.find_element(
            By.XPATH, r'/html/body/div[6]/div[1]/div/div/ul/li[15]/a').click()
        #
        wait((By.XPATH, r'/html/body/div[5]/div[1]/div/a[2]'), timeout=10)
    except:
        chongbuluo_log.log('签到元素加载失败', level='error')
        return
    try:
        # 签到
        # /html/body/div[5]/div[2]/div[1]/div[1]/a
        chongbuluo_log.log('点击签到', level='info')
        sign_in_text = browser.find_element(
            By.XPATH, r'/html/body/div[5]/div[2]/div[1]/div[1]/a').text
        if not '已签到' in sign_in_text:
            browser.find_element(
                By.XPATH, r'/html/body/div[5]/div[2]/div[1]/div[1]/a').click()
            wait((
                By.XPATH,
                r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
            ),
                 timeout=10)
            if False:
                filling_words = datetime.now().strftime('%Y-%m-%d')
            else:
                filling_words = piece_lrc()
            chongbuluo_log.log(filling_words, level='info')
            browser.find_element(
                By.XPATH,
                r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/p/textarea'
            ).send_keys(filling_words)
            browser.find_element(
                By.XPATH,
                r'/html/body/div[1]/div/table/tbody/tr[2]/td[2]/form/div/button'
            ).click()
        else:
            # print('今日已签到,无需重复签到!')
            chongbuluo_log.log('今日已签到,无需重复签到!', level='info')
    except:
        chongbuluo_log.log('签到失败', level='error')
        return

    try:
        # 刷新签到页面
        # 签到信息
        continue_days = 'NaN'
        got_bits = 'NaN'
        time.sleep(2 + random())
        wait((By.XPATH, r'/html/body/div[5]/div[1]/div/a[2]'), timeout=10)
        browser.find_element(By.XPATH,
                             r'/html/body/div[5]/div[1]/div/a[2]').click()
        continue_days = browser.find_element(
            By.XPATH,
            r'/html/body/div[5]/div[2]/div[1]/div[2]/ul/li[1]/span[1]').text
        got_bits = browser.find_element(
            By.XPATH,
            r'/html/body/div[5]/div[2]/div[1]/div[2]/ul/li[2]/span').text
        got_bits = re.sub(r'Bit', '', got_bits)
        text_temp = "\t连续签到:%5s天 \t 累计获得:%4s Bit" % (continue_days, got_bits)
        chongbuluo_log.log('自动签到成功' + '\n' + text_temp.center(40, chr(12288)) +
                           '—' * 5 + '\n',
                           level='info')
        browser.quit()
    except:
        chongbuluo_log.log('获取签到信息失败', level='error')
        return


def piece_lrc(lrc_file=r'./lrc/eason.txt'):

    emoji = [
        "😀", "😃", "😄", "😁", "😆", "😊", "🫠", "🥰", "🤩", "😛", "🤪", "😝", "🤠", "👋",
        "✋", "👌", "✌", "👏", "🙌", "🫶", "✍", "🐵", "🐒", "🐵", "🐒", "🦍", "🦧", "🐶",
        "🐕", "🦮", "🐕‍🦺", "🐩", "🐺", "🦊", "🦝", "🐱", "🐈", "🐈‍⬛", "🦁", "🐯", "🐅",
        "🐆", "🐴", "🐎", "🦄", "🦓", "🦌", "🦬", "🐮", "🐂", "🐃", "🐄", "🐷", "🐖", "🐗",
        "🐽", "🐏", "🐑", "🐐", "🐪", "🐫", "🦙", "🦒", "🐘", "🦣", "🦏", "🦛", "🐭", "🐁",
        "🐀", "🐹", "🐰", "🐇", "🐿", "🦫", "🦔", "🦇", "🐻", "🐻‍❄️", "🐨", "🐼", "🦥",
        "🦦", "🦨", "🦘", "🦡", "🐾"
    ]
    cnt = len(emoji)
    ret_lrc = "签到" + emoji[randint(0, cnt - 1)]
    # ret_lrc = ""
    # try:
    #     with open(lrc_file, encoding='utf-8', mode='r') as f:
    #         all_lines = f.readlines()
    #         line_cnt = len(all_lines)
    #         ret_lrc = all_lines[randint(0, line_cnt - 1)]
    #         ret_lrc = re.sub(r'\[\d{1,}\]:', '', ret_lrc)
    # except:
    #     ret_lrc = '感谢你特别邀请 来见证你的爱情'
    return ret_lrc


if __name__ == "__main__":
    # log_in_main_page()
    for k in range(100):
        piece_lrc(lrc_file=r'./lrc/selfpart.txt')
