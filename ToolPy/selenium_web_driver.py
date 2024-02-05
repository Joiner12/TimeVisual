# -*- coding:utf-8 -*-

from selenium import webdriver


# todo:简化封装类
class CustomSeleniumWrapper:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def find_element_by_id(self, element_id):
        return self.driver.find_element_by_id(element_id)
