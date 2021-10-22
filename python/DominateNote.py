# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:04:22 2021

@author: W-H
"""
# import dominate
# from dominate.tags import *

# baseHtml = html(body(h1('Hello, World!')))
# print(baseHtml)
import requests
import re
# %%
OriginStr = """<div class="ntopbar_loading"><img
src="http://simg.sinajs.cn/blog7style/images/common/loading.gif">加载中…</div>"""
pat = '<div class="ntopbar_loading">.*?>'
b = re.findall(pat, OriginStr)
print('re:', pat, '\n', 'match:', b)
# 打印信息:
# match: ['<div class="ntopbar_loading"><img src="http://simg.sinajs.cn/blog7style/images/common/loading.gif">']
pat = '<div.*>(.*?)</div>'
b = re.findall(pat, OriginStr)
print('re:', pat, '\n', 'match:', b)
# 打印信息:
# match: ['加载中…']
for k in range(10):
    print('\r\n')
pat = '<div class="ntopbar_loading">.*?>(.*?)</div>'
b = re.findall(pat, OriginStr)
print('match:', b)
pat = '<div class="ntopbar_loading">.*?>(.*?)</div>'
b = re.findall(pat, OriginStr, re.S)
print('match:', b)

"""
    原因说明:
    1.'.*'和'.*?'的区别,前者是贪心模式,后者是非贪心模式.通俗的说就是,贪心模式会尽可能多地匹配内容.
    e.g: <div.*>表示匹配'<div'和'>'中间的尽可能多的内容,
    a='<div class="ntopbar_loading"><img src="http://simg.sinajs.cn/blog7style/images/common/loading.gif">'
    a中满足以'<div'开头以'>'结尾的内容有两种a1,a2;
    a1 = '<div class="ntopbar_loading">'
    a2 = a,a2的字符串长度大于a1,也即其满足正则表达式的内容更多,'.*'则是匹配尽可能多的,所以'.*'匹配出来的是a2.
    '.*?'尽可能少地匹配内容,所以匹配出来的是a1.
"""

# %%
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
url = 'http://irm.cninfo.com.cn/'
res = requests.get(url, headers=headers).text
time = '<span class="question-time hidden-xs-only">(.*?).</span>'
question = '<div class="question-content pd-20 pb-10">.*?>(.*?)</div>'
question1 = '<div class="question-content" style="font-weight: normal;">.*?>(.*?)</div>'
question2 = '<div class="question-content".*>(.*?)</div>'
reply = '<div class="reply-content pd-20 pb-10">.*?>(.*?)</div>'
time = re.findall(time, res)
ques = re.findall(question, res, re.S)
ques1 = re.findall(question1, res, re.S)
ques2 = re.findall(question2, res, re.S)
rep = re.findall(reply, res, re.S)
#%% 
for i in range(len(ques)):
    ques[i] = ques[i].strip()
for j in range(len(ques1)):
    ques1[j] = ques1[j].strip()
    # rep[i]=rep[i].strip()
# %%

orgqus1 = """<div class="question-content pd-20 pb-10"><img src="http://ircsstatic.cninfo.com.cn/ircs//assets/images/question-icon.png" alt="" class="question-icon">
                                                董秘您好，请问公司截止至目前的股东户数是多少？拜托您了，万分感谢！
                                                </div>"""
# 网页源码
orgqus2 = """<div class="question-content" style="font-weight: normal;"><img src="http://ircsstatic.cninfo.com.cn/ircs//assets/images/question-icon.png" alt="" class="question-icon">
                                                请问公司的主营业务之一的游戏板块有没有元宇宙的概念？
                                                </div>"""
question = r'<div class="question-content pd-20 pb-10">.*?>(.*?)</div>'
# 有效
question1 = r'<div class="question-content" style="font-weight: normal;">.*?>(.*?)</div>'
# 无效
question1 = '<div class="question-content" style="font-weight:normal;">.*?>(.*?)</div>'
question2 = '<div class="question-content".*>(.*?)</div>'
ques = re.findall(question, orgqus1, re.S)
ques1 = re.findall(question1, orgqus2, re.S)
ques2 = re.findall(question2, res, re.S)
print(ques2)
