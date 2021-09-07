# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:01:12 2021

@author: W-H
"""
import requests
import csv
import parsel
import re
# from pandas import
url = 'http://data.eastmoney.com/report/zw_stock.jshtml?encodeUrl=tZCeKHMdSi09TERE/g/WdMgSdW7adh8t+BT3DNkbRyg='
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
response = requests.get(url=url, headers=headers)
html_data = response.text
# 打印检查爬取的html(网页)

selector = parsel.Selector(html_data)
# 1.main-left标签只有一个 不需要使用递归
# 2.'.detail-header h1':混合选择器,选择属性为detail-header下的<h1>标签
title = selector.css('.detail-header h1::text').get()
# 使用正则表达式替换换行符'\n',' '
title = re.sub(r'\n| ','',title)
content = selector.css('.newsContent p::text').getall()
content = [re.sub(r'\n| ','',x) for x in content] 
reportInfo = selector.css('.report-infos span::text').getall()
reportInfo = [re.sub(r'\n| ','',x) for x in reportInfo]
# 检查爬取结果
print(title)
print(reportInfo[0],reportInfo[1])
for k in content:
    print(k)
# with open('yanbao.csv', mode='a', encoding='utf-8', newline='') as f:
#     csv_write = csv.writer(f)
#     csv_write.writerow([title, content])
