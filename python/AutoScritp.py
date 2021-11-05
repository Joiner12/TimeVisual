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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from numpy import random
import time
def testWebdriver():
    print('check for to do list')
    """
    embeded function
    """
    def wait(locator, timeout=2):
        WebDriverWait(browser, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator))

    TargetBaseUrl = r'http://172.18.0.28:8080/cas/login?service=http://172.18.0.29/cas#/portal/index'
    chromeOptions = Options()
    chromeOptions.add_argument('headless')
    browser = webdriver.Chrome(
        executable_path=r"D:\Code\TimeVisual\python\chromedriver.exe", options=chromeOptions)

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

    try:
        while True:
            # scroll for load element js
            browser.execute_script("window.scrollBy(0,3000)")
            wait((By.XPATH,
                  r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a'))
            elementUpcoming = browser.find_element_by_xpath(
                r'//*[@id="app"]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/ul/li[1]/a')
            print(elementUpcoming.text)
            browser.execute_script("arguments[0].click();", elementUpcoming)
            time.sleep(3+random.rand())
            all_h = browser.window_handles
            browser.switch_to.window(all_h[1])
            browser.execute_script("window.scrollBy(0,3000)")
            time.sleep(3+random.rand())
            wait((By.CSS_SELECTOR, '.submit_btn.form_btn1'))
            browser.execute_script(
                "arguments[0].click();", browser.find_element_by_css_selector('.submit_btn.form_btn1'))
            time.sleep(1+random.rand())
    except:
        print('empty to do list')

    browser.quit()


if __name__ == "__main__":
    testWebdriver()
