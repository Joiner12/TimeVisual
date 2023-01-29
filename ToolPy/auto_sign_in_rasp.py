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
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from random import randint, random
import re
import time
import sys
from logger import Logger
import requests

chongbuluo_log = Logger()


def log_in_main_page():
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    TargetBaseUrl = r'https://www.chongbuluo.com/'
    chongbuluo_log.log('开始自动签到，完成配置', level='info')
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
            s = Service(executable_path=
                        r'/home/smileface/Desktop/chongbuluo/chromedriver')
            browser = webdriver.Chrome(service=s)
            chongbuluo_log.log('browser驱动配置完成', level='info')
        else:
            pass
    except:
        chongbuluo_log.log('browser驱动初始化失败', level='error')
        return
    # 检查登陆状态
    logpage = requests.get(r'https://www.chongbuluo.com/')
    # 已登陆
    if logpage.status_code == 200:
        chongbuluo_log.log('网络连接状态：正常', level='info')
    else:
        chongbuluo_log.log('网络连接状态：异常', level='error')
        return
    # ---
    try:
        # browser.set_window_size(200, 200)
        chongbuluo_log.log('输入账号密码', level='info')
        browser.get(TargetBaseUrl)
        # log in
        browser.find_element(By.CSS_SELECTOR,
                             r'#welcome > a:nth-child(1)').click()
        # 等待加载f
        wait((By.XPATH, r'//*[@id="main_message"]/div/div[1]/h3'))
        browser.find_element(By.NAME, "username").clear()
        browser.find_element(By.NAME, "username").send_keys('Risky_JR')
        browser.find_element(By.NAME, "password").clear()
        browser.find_element(By.NAME, "password").send_keys('Risky11#')
        browser.find_element(By.NAME, 'loginsubmit').click()
    except:
        chongbuluo_log.log('输入账号密码失败', level='error')
        return

    try:
        # 签到页面
        chongbuluo_log.log('查找签到按钮', level='info')
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
        # print('—' * 59 + '\n', text_temp.center(40, chr(12288)), '—' * 59)
        chongbuluo_log.log('自动签到成功' + '\n' + text_temp.center(40, chr(12288)) +
                           '—' * 5 + '\n',
                           level='info')
        browser.quit()
    except:
        chongbuluo_log.log('获取签到信息失败', level='error')
        return


def piece_lrc(lrc_file=r'./lrc/eason.txt'):
    """
        emoji = ["🐷", "🐖", "🐗",
             "🐽", "🐏", "🐑", "🐐", "🐪", "🐫", "🦙", "🦒", "🐘", "🦣", "🦏", "🦛", "🐭", "🐁",
             "🐀", "🐹", "🐰", "🐇", "🐿", "🦫", "🦔", "🦇", "🐻", "🐻‍❄️", "🐨", "🐼", "🦥",
             "🦦", "🦨", "🦘", "🦡", "🐾"
             ]
    """
    charc_emoji = [
        "o(〃'▽'〃)o", "（￣︶￣）↗", "<（￣︶￣）>", "ʕ•̫͡• ʔ", "ˁ῁̭ˀ", "ˁ῁̬ˀ", "ˁ῁̼ˀ",
        "ˁ῁̩ˀ", "ˁ῁̥ˀ", "ˁ῁̱ˀ", "ˁ῁̮ˀ", "♡", " .^◡^.", "ᵔ.ᵔ", "ᵔ◡ᵔ", "ʕง•ᴥ•ʔง",
        "ʕ•ᴥ•ʔ", "ʕᵔᴥᵔʔ", "'◡'", "ʕ•̫͡• ʔ", "ʕ•͓͡•ʔ", "ʕ•̫͡•ʔ", "ʕ•̫͡•ཻʔ",
        "ヽ(✿ﾟ▽ﾟ)ノ", "╰(*°▽°*)╯", "♪(^∇^*)", " (　ﾟ∀ﾟ) ﾉ♡"
    ]
    cnt = len(charc_emoji)
    ret_lrc = "签到 " + charc_emoji[randint(0, cnt - 1)]
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
    log_in_main_page()
    # for k in range(10):
    #     print(piece_lrc(lrc_file=r'./lrc/selfpart.txt'))
