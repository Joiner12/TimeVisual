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
import re
from selenium.webdriver.common.action_chains import ActionChains
# 日志文件
lg = Logger(logging_service='oa')


def testWebdriver():
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    lg.log("自动公文系统启动", "info")
    # 检查网络连接状态
    TargetBaseUrl = r'http://172.18.0.28:8080/cas/login?service=http://172.18.0.29/cas#/portal/index'
    if not requests.get(TargetBaseUrl).status_code == 200:
        lg.log("网络连接失败", "error")
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
        "ms:edgeOptions": {
            'extensions': [],
            'args': [
                '--headless'
                # '--disable-gpu',
                # '--remote-debugging-port=9222',
            ]
        }
    }
    try:
        browser = webdriver.Edge(
            executable_path=
            r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
            capabilities=EDGE)
    except:
        lg.log("edge驱动配置失败", "error")
    try:
        browser.get(TargetBaseUrl)
    except:
        lg.log("目标主页连接失败", "error")

    # login status
    try:
        longInButtonId = "normalLoginButton"
        wait((By.ID, longInButtonId))
        browser.find_element(By.ID, longInButtonId)
    except:
        lg.log("登录按键查找失败", "error")
    # send userkey
    try:
        browser.find_element(By.ID, "username").clear()
        browser.find_element(By.ID,
                             "username").send_keys(os.getenv('OA_USERNAME'))
        browser.find_element(By.ID, "password").clear()
        # browser.find_element(By.ID, "password").send_keys(os.getenv('OA_PASSWORD'))
        browser.find_element(By.ID, "password").send_keys('chinamobile_5')
        browser.find_element(By.ID, longInButtonId).click()
    except:
        lg.log("账号密码错误", "error")
    # dialog-content dialogin
    if False:
        # 方法一:设置弹窗为不可见
        close_dialog_js = 'document.getElementsByClassName("dialog-content dialogin").style.display="none";'
        browser.execute_script(close_dialog_js)
    else:
        # 方法二:空白处点击
        ActionChains(browser).move_by_offset(1, 1).click().perform()

    # loop_cnt = 0
    # while True:
    #     ret = click_upcoming_item_v2(browser)
    #     browser = ret[0]
    #     loop_cnt += 1
    #     if not ret[1] or loop_cnt > 10:
    #         break
    try:
        loop_cnt = 0
        while True:
            ret = click_upcoming_item_v2(browser)
            browser = ret[0]
            loop_cnt += 1
            if not ret[1] or loop_cnt > 10:
                break
    except:
        pass
    lg.info("监测完成", "info")
    browser.quit()


def click_upcoming_item_v2(browser, *args, **kwargs):
    """
    embeded function
    """

    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    # wait((
    #     By.XPATH,
    #     r'//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/div[1]'
    # ))
    time.sleep(3 + random.rand())
    # 方法二:空白处点击

    ActionChains(browser).move_by_offset(1, 1).click().perform()
    time.sleep(1 + random.rand())
    try_new_flag = False
    try:
        more_todo_elemet = browser.find_element(
            By.XPATH,
            r'/html/body/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/a[2]'
            #r'/html/body/div/div/div/div[2]/div[3]/div/div[1]/div/div/div/div[1]/a[2]'
        )
        more_todo_elemet.click()
    except:
        try_new_flag = True
        lg.log("点击/*更多*/按钮错误", "error")

    if try_new_flag:
        try:
            more_todo_elemet = browser.find_element(
                By.XPATH,
                # r'/html/body/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/a[2]'
                r'/html/body/div/div/div/div[2]/div[3]/div/div[1]/div/div/div/div[1]/a[2]'
            )
            more_todo_elemet.click()
        except:
            lg.log("点击/*更多*/按钮错误", "error")
    # 切换到代办窗口
    all_h = browser.window_handles
    main_window = all_h[0]
    browser.switch_to.window(all_h[1])
    time.sleep(3 + random.rand())

    # 处理动态Item序号问题
    li_num = -1
    try:
        for k in range(1, 5, 1):
            x_path = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[1]/ul/li[%d]' % (
                k)
            li_item_name = browser.find_element(By.XPATH, x_path).text
            ret_re = re.split(" ", li_item_name)
            if ret_re[0] == "公文系统":
                li_num = k
                break
    except:
        return browser, 0
    # 判断li_num是否有效
    if -1 == li_num:
        lg.log("公文系统index查找失败", "error")
        return
    x_path = '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[1]/ul/li[%d]' % (
        li_num)
    doc_sys = browser.find_element(By.XPATH, x_path).text
    ret_re = re.split(" ", doc_sys)
    doc_num = int(ret_re[-1])
    if not doc_num == 0 and "公文系统" in ret_re[0]:
        # 切换到公文系统
        browser.find_element(By.XPATH, x_path).click()
        time.sleep(1 + random.rand())
        # 点击处理
        _处理按键 = browser.find_element(
            By.XPATH,
            r'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/button'
        )
        browser.execute_script("arguments[0].click();", _处理按键)
        _公文名 = browser.find_element(
            By.XPATH,
            r'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/a'
        ).text

        time.sleep(2 + random.rand())
        # 窗口切换
        all_h = browser.window_handles
        browser.switch_to.window(all_h[2])
        time.sleep(2 + random.rand())
        browser.execute_script("window.scrollBy(0,3000)")
        # wait((By.CSS_SELECTOR, '.submit_btn.form_btn1'))
        # //*[@id="section-4"]/div/div[1]/div[3]/span[2]/table/tbody/tr/td[1]/textarea
        _处理意见 = browser.find_element(
            By.XPATH,
            r'//*[@id="section-4"]/div/div[1]/div[3]/span[2]/table/tbody/tr/td[1]/textarea'
        )
        if len(_处理意见.text) == 0:
            _已阅 = browser.find_element(By.XPATH, r'//*[@id="i"]')
            browser.execute_script("arguments[0].click();", _已阅)
        browser.execute_script(
            "arguments[0].click();",
            browser.find_element_by_css_selector('.submit_btn.form_btn1'))
        lg.log("\r\n" + _公文名, "info")
        doc_num -= 1
    else:
        doc_num = 0
    # 关闭多余窗口
    all_h = browser.window_handles
    for window_cur in all_h:
        if window_cur != main_window:
            browser.switch_to.window(window_cur)
            browser.close()
    browser.switch_to.window(main_window)
    return browser, doc_num


if __name__ == "__main__":
    testWebdriver()