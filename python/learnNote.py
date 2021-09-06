# %% :和→用法解释
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from pyecharts.charts import Bar
from random import randint
import time
from readDataFromExcel import DataFromExcel
from datetime import datetime
import numpy as np
import pandas as pd
from typing import Any, Optional, Sequence, Tuple, Union
# %%


def fund(a,
         font_style: Optional[str] = None,
         font_weight: Optional[str] = None,
         font_family: Optional[str] = None):
    print(a)
    opts: dict = {
        'font_style': font_style,
        'font_weight': font_weight,
        'font_family': font_family
    }
    print(opts)


fund(1)

# %% dataframe 数据拼接
"""
https://blog.csdn.net/sc179/article/details/108169436

"""
# 单列的内连接
# 定义df1
df1 = pd.DataFrame({
    'alpha': ['A', 'B', 'B', 'C', 'D', 'E'],
    'feature1': [1, 1, 2, 3, 3, 1],
    'feature2': ['low', 'medium', 'medium', 'high', 'low', 'high']
})
# 定义df2
df2 = pd.DataFrame({
    'alpha': ['A', 'A', 'B', 'F'],
    'pazham': ['apple', 'orange', 'pine', 'pear'],
    'kilo': ['high', 'low', 'high', 'medium'],
    'price': np.array([5, 6, 5, 7])
})
# 基于共同列alpha的内连接
df3 = pd.merge(df1, df2, how='inner', on='alpha')

print(df1)
print(df2)
print(df3)

#
df1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
    'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

# lsuffix和rsuffix设置连接的后缀名
df3 = df1.join(df2, lsuffix='_caller', rsuffix='_other', how='inner')

print(df1)
print(df2)
print(df3)

#
df1 = pd.Series([1.1, 2.2, 3.3], index=['i1', 'i2', 'i3'])
df2 = pd.Series([4.4, 5.5, 6.6], index=['i2', 'i3', 'i4'])
print(df1)
print(df2)

# 行拼接
df3 = pd.concat([df1, df2])

print(df1)
print(df2)
print(df3)

# %% 动态修改dataframe
"""
https://blog.csdn.net/qq_39783601/article/details/104436303
https://www.yiibai.com/pandas/python_pandas_dataframe.html
"""

initData = {'起始': 1, '终止': 2, '事件': 3, '时长': 5}
testData = pd.DataFrame(columns=['起始', '终止', '事件', '时长', 'other'])
testData = testData.append(initData, ignore_index=True)

# %%

datetime.now()
a = datetime.strptime("2021-8-1", '%Y-%m-%d')
print(datetime.now() > datetime.strptime("2021-08-8", '%Y-%m-%d'))

# %%
# -*- coding:utf-8 -*-
"""
    panda data frame learn
    ref:
    https://blog.csdn.net/xtfge0915/article/details/52938740
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.empty.html
"""
# import pandas as pd
""" 
    数据读取——single sheet
"""
testData = DataFromExcel("..//data//Commuter.xlsx").getData()
testData = testData['Sheet1']
print(testData)
# 通过列名字索引
# d1 = testData['日期']
# print(d1, type(d1))
# d2 = testData.日期
# d3 = (d2[1])

# 通过列号读取数据
print(testData.iloc[:, 7])
print(testData.iloc[:, 3:])
print(testData.iloc[:, 5:7])

# 通过行号读取数据
print(testData.iloc[1, :])
print(testData.iloc[1, 5])

# series to list
print(testData.iloc[:, 7].tolist())
# %%
test1 = pd.DataFrame({'a': []})
print(test1.empty)
# %%
""" 
    数据读取——multiple sheet
"""
df_1 = DataFromExcel(r"D:\Code\HouseMonitor\TimeVisual\data\gatte-test.xlsx")
exlsData_1 = df_1.getData()
if isinstance(exlsData_1, dict):
    keysDict = exlsData_1.keys()
    for k in keysDict:
        print(k)
    # sheet_20210315 = exlsData_1['2021-03-15']
# print(sheet_20210315)

# %% string split
orStr = "data-data-code-data-code-data-code-visual-code-info-visual-code-visual-code-visual-code-visual-code-git-visual-code-visual-code-AOA\AOD-visual-code-visual-code-visual-code-visual-code-AOA\AOD-AOA\AOD-AOA\AOD-AOA\AOD-AOA\AOD-78-AOA\AOD-开会-paper-发票-visual-code-visual-code-visual-code-visual-code-visual-code-motion-discussion-visual-code"
splitStr = orStr.split("-")
strList = ['从前', '初识', '这', '世界']
prtStr = str()
for L in strList:
    prtStr += (L+"-")
print(prtStr)

# %% sleep
"""
http://c.biancheng.net/view/2612.html
"""
print(datetime.now().strftime('%M-%S'))
for k in range(10):
    time.sleep(randint(1, 4))
    print(datetime.now().strftime('%M-%S'))

# %% numpy
x = np.linspace(1, 5, 5)
x1 = x.tolist()
y1 = np.zeros([1, len(x)])
# %%
print("check lib finished")
# %% set_xaxis label

# Load a numpy structured array from yahoo csv data with fields date, open,
# close, volume, adj_close from the mpl-data/example directory.  This array
# stores the date as an np.datetime64 with a day unit ('D') in the 'date'
# column.
data = [7, 10, 8, 11, 5, 9, 9, 6]

fig, axs = plt.subplots(3, 1, figsize=(6.4, 7), constrained_layout=True)
# common to all three:
for ax in axs:
    ax.plot('date', 'adj_close', data=data)
    # Major ticks every half year, minor ticks every month,
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.grid(True)
    ax.set_ylabel(r'Price [\$]')

# different formats:
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')

ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(
    mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02,
             fontsize='medium')
# Text in the x axis will be displayed in 'YYYY-mm' format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
# Rotates and right-aligns the x labels so they don't crowd each other.
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')

plt.show()

# %%
# 生成横纵坐标信息
startTick_x = ['2021-08-09 09:00:00', '2021-08-09 09:45:00',
               '2021-08-09 11:11:00', '2021-08-09 14:30:00',
               '2021-08-09 15:18:00',
               '2021-08-09 16:40:00', '2021-08-09 17:19:00'],
eventName_x = ['开会', '发票', 'visual-code', '舆情分析',
               'AOA-Paper', 'AOA-Paper', 'visual-code'],
eventLast_x = [30, 78, 33, 47, 69, 39, 15]
dates = ['01/02/1991', '01/03/1991', '01/04/1991']
xs = [datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
ys = range(len(xs))
# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# Plot
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()

# %%
start = datetime.strptime('2021-08-09 07:00:00', '%Y-%m-%d %H:%M:%S')
stop = start+timedelta(hours=20)
detimestr = stop.strftime("%Y-%m-%d %H:%M:%S")
fig, ax = plt.subplots(figsize=(24, 24*0.618),
                       facecolor='#D6D7C5', dpi=300)
ax.broken_barh([(start, (stop-start))],
               (-1/2, 1), alpha=.5, facecolors='#ace9e8', edgecolors='white')
plt.show()
#%% demo()
"""Demonstrate how each CapStyle looks for a thick line segment."""
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4, 1.2))
ax = fig.add_axes([0, 0, 1, 0.8])
ax.set_title('Cap style')

for x, style in enumerate(['butt', 'round', 'projecting']):
    ax.text(x+0.25, 0.85, style, ha='center')
    xx = [x, x+0.5]
    yy = [0, 0]
    ax.plot(xx, yy, lw=12, color='tab:blue', solid_capstyle=style)
    ax.plot(xx, yy, lw=1, color='black')
    ax.plot(xx, yy, 'o', color='tab:red', markersize=3)
ax.text(2.25, 0.55, '(default)', ha='center')

ax.set_ylim(-.5, 1.5)
ax.set_axis_off()
fig.show()