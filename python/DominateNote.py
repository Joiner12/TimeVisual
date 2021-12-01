# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:04:22 2021

@author: W-H
"""
# import dominate
# from dominate.tags import *

# baseHtml = html(body(h1('Hello, World!')))
# print(baseHtml)
from dominate.util import text
from dominate.tags import *
import dominate
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
# %%
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

# %%
print(html(body(h1('Hello, World!'))))
bd = body()
for item in range(4):
    bd += div('Item #', item)
print(bd)
menu_items = (['home', r'/home/'], ['about', '/about'])
print(ul(li(a(name, href=link), __pretty=False) for name, link in menu_items))
_html = html()
_head = _html.add(head(title("Simple Document Tree")))
_body = _html.add(body())
header = _body.add(div(id='header'))
content = _body.add(div(id='content'))
footer = _body.add(div(id='footer'))
print(_html)

_html = html()
_head, _body = _html.add(head(title('Simple Document Tree')), body())
names = ['header', 'content', 'footer']
header, content, footer = _body.add([div(id=name) for name in names])
# print(_html)
# %%
header = div('Test')
print(header)
header[0] = 'Hello World'
print(header)
print(comment('this is a piece of commit'))
print(comment(p('Upgrade to newer IE!'), condition='lt IE9'))

# %%
print(r'--------------')
a = div(span('Hello World'))
print(a.render())
print(r'--------------')
print(a.render(pretty=False))
print(r'--------------')
print(a.render(indent='\t'))
print(r'--------------')
a = div(span('Hello World'), __pretty=False)
print(a.render())
d = div()
with d:
    hr()
    p("Test")
    br()
print(r'--------------')
print(d.render())
print(r'--------------')
print(d.render(xhtml=True))

# %%
a = div(span('Hello World'))
print(a.render(), '\n', type(a.render()))
with open('test.html', mode='w', encoding='utf-8') as f:
    f.write(a.render())
# %%
a = [200.00, 53.00, 59.75, 55.56, 42.06, 51.73,
     54.78, 68.58, 128.00, 210.00, 150.00]
print(sum(a))

# %%
# 创建一个无序列表标签
h = ul()
# 使用with给无序列表添加列表项目
with h:
    li('One')
    li('Two')
    li('Three')

print(h)
# %%
h = html()
with h.add(body()).add(div(id='content')):
    h1('Hello World!')
    p('Lorem ipsum ...')
    with table().add(tbody()):
        l = tr()
        l += td('One')
        l.add(td('Two'))
        with l:
            td('Three')

print(h)
# %%
para = p("This is a paragraph,", __pretty=False)
print(para)
with para:
    text('Have a look at our ')
    a('other products', href='/products')

print(para)
#%% 
def greeting(name):
    with div() as d:
        p('Hello, %s' % name)
    return d
D1 = greeting('Bob')
with D1:
    h1('DEL')
print(greeting('Bob'))
print(D1)
#%% 
@div
def greeting(name):
    p('Hello %s' % name)
print(greeting('Bob'))
#%% 
@div(h2('Welcome'), cls='greeting')
def greeting(name):
    p('Hello %s' % name)

print(greeting('Bob'))
#%% 
"""
天气预报温度和体感温度
reference:https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
"""
import math
# NOAA体感温度计算简化公式,T:(天气预报温度)1.5米高处的气温(摄氏度)，RH:相对湿度(0~100或者0~1)
def calc_heat_index(T, RH):
    if RH < 1:
        RH *= 100
    T = 1.8 * T + 32
    HI = 0.5 * (T + 61 + (T - 68) * 1.2 + RH * 0.094)
    if HI >= 80:  # 如果不小于 80华氏度 则用完整公式重新计算
        HI = -42.379 + 2.04901523 * T + 10.14333127 * RH - .22475541 * T * RH \
             - .00683783 * T * T - .05481717 * RH * RH + .00122874 * T * T * RH \
             + .00085282 * T * RH * RH - .00000199 * T * T * RH * RH
        if RH < 13 and 80 < T < 112:
            ADJUSTMENT = (13 - RH) / 4 * math.sqrt((17 - abs(T - 95)) / 17)
            HI -= ADJUSTMENT
        elif RH > 85 and 80 < T < 87:
            ADJUSTMENT = (RH - 85) * (87 - T) / 50
            HI += ADJUSTMENT
    return round((HI - 32) / 1.8, 2)
# 
T = 10
RH = 0.75
heat_index = calc_heat_index(T,RH)
print('天气预报温度:%0.2f,相对湿度:%0.2f\n体感温度:%0.2f'%(T,RH,heat_index))