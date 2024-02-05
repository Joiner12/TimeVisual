# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time, json

# workspace
cmd = """cd D:\Code\TimeVisual\ToolPy """
os.system(cmd)

# 1.初始化selenium 驱动
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "",
    "platform": "WINDOWS",
    # "ms:edgeOptions": {"extensions": [], "args": ["--headless"]},
    "ms:edgeOptions": {"extensions": []},
}
browser = webdriver.Edge(
    executable_path=r"D:\Code\TimeVisual\ToolPy\driver\msedgedriver.exe",
    capabilities=EDGE,
)
browser.get("https://www.bilibili.com")
try:
    # 读取cookie的json文件
    f = open(r"D:\Code\TimeVisual\ToolPy\cookie.json", "r")
    list_cookies = json.loads(f.read())  # 读取文件中的cookies数据

    # 将cookie塞到浏览器中，绕过登录
    for cookie in list_cookies:
        browser.add_cookie(cookie)  # 将cookies数据添加到浏览器
except:
    pass
# 2.打开主页
# browser.get("https://space.bilibili.com/403940805/video")
browser.get("https://space.bilibili.com/1735431742/video")
time.sleep(2)
browser.refresh()
# https://space.bilibili.com/403940805/video?tid=0&pn=4&keyword=&order=pubdate
# 3.翻页
with open("bilibili_video_info.txt", "w", encoding="utf-8") as file:
    pass

for _ in range(58):
    video_info = []
    time.sleep(10)
    # 循环获取每一个视频的封面和描述
    video_elements = browser.find_elements_by_css_selector(".small-item")
    for i in range(len(video_elements)):
        # 重新查找视频元素
        video_elements = browser.find_elements_by_css_selector(".small-item")
        video_element = video_elements[i]
        cover = video_element.find_element_by_css_selector(".cover img").get_attribute(
            "src"
        )
        video_link = video_element.find_element_by_css_selector(".title").get_attribute(
            "href"
        )
        description = video_element.find_element_by_css_selector(".title").text
        print(f"封面链接：{cover}\r\n描述：{description}\r\n视频链接：{video_link}")
        video_info.append(
            {"cover_url": cover, "description": description, "video_link": video_link}
        )
        time.sleep(1)
    # 保存至文档
    with open("bilibili_video_info.txt", "a", encoding="utf-8") as file:
        for info in video_info:
            file.write(
                f'封面链接: {info["cover_url"]}\n描述: {info["description"]}\n视频链接: {info["video_link"]}\n'
            )

    # 点击下一页按钮
    next_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".be-pager-next"))
    )
    next_button.click()
    time.sleep(10)
    browser.refresh()


# 退出
browser.quit()
