#-*- utf-8 -*-
"""
    功能:
        1.读取每天的事件-时间信息;
        2.使用matplotlib绘制时间-事件-时长极坐标图;
        3.极坐标图设计思路:root/design.drawio
        4.以一定方式渲染出来
    todo:
        (1) 原始数据时间长度解析问题 √
        (2) 默认读取时间,脚本运行时间 √
        (3) 异常数据处理nan nat √
        (4) 源数据拷贝 √
        (5) 输出文件路径 √
        (6) ValueError: Wedge sizes 'x' must be non negative values √
        (7) 命令行调用输入参数
"""
import shutil
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os import path
from datetime import datetime, date, timedelta, time
from io import BytesIO
from lxml import etree
import base64

plt.rcParams["font.sans-serif"] = ["SimHei"]  #设置字体
plt.rcParams["axes.unicode_minus"] = False  #该语句解决图像中的“-”负号的乱码问题


def DrawPloarBar(base_start_tick,
                 event_name=["a", "b", "c", "d", "e"],
                 duration=[1, 2, 2, 3, 4],
                 **kw):
    x_circle = np.sin(
        np.arange(0, 2 * np.pi + 2 * np.pi / 100, 2 * np.pi / 100))
    y_circle = np.cos(
        np.arange(0, 2 * np.pi + 2 * np.pi / 100, 2 * np.pi / 100))

    if int(base_start_tick.hour / 9) == 0:
        base_time_label = ["08:30", "11:30", "14:30", "17:30"]
    else:
        base_time_label = ["09:00", "12:00", "15:00", "18:00"]

    fig, ax = plt.subplots(dpi=150, frameon=False)
    # 颜色设置
    wedges_color = list()
    for item in event_name:
        if item == "nothing":
            wedges_color.append((255 / 255, 235 / 255, 205 / 255))
        else:
            color_a = np.random.randint(0, 230, (3, 1)).tolist()
            for k in range(len(color_a)):
                color_a[k] = color_a[k][0] / 255
            wedges_color.append(color_a)
    # 圆形外框
    ax.plot(x_circle, y_circle)

    # 绘制按照时间顺序的饼状图
    wedges, texts = ax.pie(duration,
                           wedgeprops=dict(width=0.9),
                           startangle=90,
                           counterclock=False,
                           colors=wedges_color)
    # 十字箭头
    arrow_comp = 0.2
    ax.annotate(base_time_label[0],
                xy=(0, -0.01),
                color="#E0C84F",
                weight="bold",
                xytext=(0, 1 + arrow_comp),
                arrowprops=dict(arrowstyle="<-",
                                connectionstyle="arc3",
                                ec="#E0C84F"),
                horizontalalignment='center',
                verticalalignment='bottom')

    # 时间箭头标注
    ax.annotate(base_time_label[1],
                xy=(-0.01, 0),
                color="#E0C84F",
                weight="bold",
                xytext=(1 + arrow_comp, 0),
                arrowprops=dict(arrowstyle="<-",
                                connectionstyle="arc3",
                                ec="#E0C84F"),
                horizontalalignment='left',
                verticalalignment='center')

    ax.annotate(base_time_label[2],
                xy=(0, 0.01),
                xytext=(0, -1 * (1 + arrow_comp)),
                color="#E0C84F",
                weight="bold",
                arrowprops=dict(arrowstyle="<-",
                                connectionstyle="arc3",
                                ec="#E0C84F"),
                horizontalalignment='center',
                verticalalignment='top')

    ax.annotate(base_time_label[3],
                xy=(0, 0),
                xytext=(-1 * (1 + arrow_comp), 0),
                color="#E0C84F",
                weight="bold",
                arrowprops=dict(arrowstyle="<-",
                                connectionstyle="arc3",
                                ec="#E0C84F"),
                horizontalalignment='right',
                verticalalignment='center')

    # 调整饼状图属性

    # nothing标签的块不进行标注
    exclude_index = [
        i for i, x in list(enumerate(event_name)) if x == "nothing"
    ]

    # 添加标签
    for i, p in enumerate(wedges):
        if i in exclude_index:
            continue

        # 标注外框属性
        bbox_props = dict(boxstyle="round,pad=0.3",
                          fc=wedges_color[i],
                          ec=wedges_color[i],
                          lw=0.3,
                          alpha=0.3)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                  bbox=bbox_props,
                  zorder=0,
                  va="center")

        # 标注
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate("%s:%d" % (event_name[i], duration[i]),
                    xy=(x, y),
                    xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment,
                    fontsize=8,
                    **kw)
    # 坐标轴设置
    font = {
        'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 16,
    }

    ax.set_title(
        "%d-%d-%d" %
        (base_start_tick.year, base_start_tick.month, base_start_tick.day),
        fontdict=font)
    ax.axis("equal")
    ax.set(xlim=(-2, 2), ylim=(-2, 2))

    # ax.axis("off")
    # plt.show()
    figuer2web(plt)


"""
    功能:
        figure对象输出为网页
"""


def figuer2web(fig,
               tarhtml=r'C:\Users\W-H\Desktop\DailyPie.html',
               *args,
               **kwargs):
    # figure 保存为二进制文件
    buffer = BytesIO()
    fig.savefig(buffer)
    plot_data = buffer.getvalue()

    # 图像数据转化为 HTML 格式
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    iris_im = """<div style="text-align:center;"><img src="%s"></div>""" % imd

    root = "<title>Iris Dataset</title>"
    root = root + iris_im  #将多个 html 格式的字符串连接起来

    # lxml 库的 etree 解析字符串为 html 代码，并写入文件
    html = etree.HTML(root)
    tree = etree.ElementTree(html)
    tree.write(tarhtml)


"""
    功能:
        读取指定excel文件的内容,并将数据转换为特定格式
"""


def readDatafromXlsx(srcfile=r'D:\Code\TimeVisual\data\gatte.xlsx',
                     *args,
                     **kwargs):
    if not path.isfile(srcfile):
        return None
    df = pd.read_excel(srcfile, sheet_name=-2, usecols=[0, 1, 2, 3])
    return df


def getDateSpecTime(data,
                    startDay: str = "today",
                    endDay: str = "today",
                    **kw):
    setTimeStrFormat = '%Y-%m-%d'
    retSegData = pd.DataFrame(
        columns=['起始', '终止', '事件', '时长', 'start_gap_base', 'end_gap_base'])
    if startDay == "today":
        startDay_i = datetime.combine(date.today(), datetime.min.time())
    else:
        startDay_i = datetime.strptime(startDay, setTimeStrFormat)
    endDay_i = datetime.combine(date.today(),
                                datetime.min.time()) + timedelta(days=1)
    # 筛选固定时间段内数据
    curSheet = data
    startTickList = curSheet['起始'].tolist()
    for j in startTickList:
        # year month day
        jJudge = j.strftime(setTimeStrFormat)
        jJudge = datetime.strptime(jJudge, setTimeStrFormat)

        if jJudge >= startDay_i and jJudge <= endDay_i:
            curIndex = startTickList.index(j)

            retSegData = retSegData.append(
                {
                    '起始': curSheet.iloc[curIndex, 0],
                    '终止': curSheet.iloc[curIndex, 1],
                    '事件': curSheet.iloc[curIndex, 2],
                    '时长': curSheet.iloc[curIndex, 3],
                },
                ignore_index=True)

    # 起始基准时间
    startTickBase = datetime.combine(
        date(startDay_i.year, startDay_i.month, startDay_i.day), time(9, 0, 0))
    if retSegData.iloc[0, 0] < startTickBase:
        startTickBase = datetime.combine(
            date(startDay_i.year, startDay_i.month, startDay_i.day),
            time(8, 30, 0))
    for index, row in retSegData.iterrows():
        retSegData.iloc[index, 4] = (retSegData.iloc[index, 0] -
                                     startTickBase).seconds
        retSegData.iloc[index, 5] = (retSegData.iloc[index, 1] -
                                     startTickBase).seconds

    # 转换成[event,duration]列表
    event_duration = list()
    for k in range(retSegData.shape[0]):
        if k == 0:
            data_temp = ['nothing', retSegData.iloc[k, 4] / 60]
            event_duration.append(data_temp)
            data_temp = [retSegData.iloc[k, 2], retSegData.iloc[k, 3]]
            event_duration.append(data_temp)
        elif k == retSegData.shape[0] - 1:
            # 可能最后一行存在NoneType问题
            data_temp = [
                'nothing',
                (retSegData.iloc[k, 4] - retSegData.iloc[k - 1, 5]) / 60
            ]
            event_duration.append(data_temp)

            if retSegData.iloc[k, 1] >= endDay_i:
                data_temp = [
                    retSegData.iloc[k, 2],
                    (endDay_i - retSegData.iloc[k, 0]).seconds / 60
                ]
                event_duration.append(data_temp)
            else:
                data_temp = [retSegData.iloc[k, 2], retSegData.iloc[k, 3]]
                event_duration.append(data_temp)
                data_temp = [
                    'nothing', (endDay_i - retSegData.iloc[k, 1]).seconds / 60
                ]
                event_duration.append(data_temp)

        else:
            data_temp = [
                'nothing',
                (retSegData.iloc[k, 4] - retSegData.iloc[k - 1, 5]) / 60
            ]
            event_duration.append(data_temp)
            data_temp = [retSegData.iloc[k, 2], retSegData.iloc[k, 3]]
            event_duration.append(data_temp)

    return (retSegData, startTickBase, event_duration)


"""
    功能:
        拷贝源文件
"""


def copy_file(srcfile=r"E:\Notes\gatte.xlsx",
              tarfile=r'D:\Code\TimeVisual\data\gatte.xlsx'):
    f1 = open(srcfile, "rb")
    f2 = open(tarfile, "wb")
    shutil.copyfileobj(f1, f2, length=1024)
    f1.close()
    f2.close()


if __name__ == "__main__":
    copy_file()
    if True:
        # 读取原始数据
        df = readDatafromXlsx()
        # 截取指定时间的数据段
        # df = getDateSpecTime(df)
        df = getDateSpecTime(df, startDay="2022-9-17")
        event_name = []
        event_duration = []
        for x in df[2]:
            event_name.append(x[0])
            event_duration.append(x[1])
        DrawPloarBar(df[1], event_name, event_duration)
