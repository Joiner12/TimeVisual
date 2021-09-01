# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:35:53 2021

@author: Peace4Lv
"""

from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts
from os import path
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime, timedelta

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False


def DrawImage(imgUrl="../html/pic/horizontalLine.png"):
    image = Image()
    # check file exists
    if not path.isfile(imgUrl):
        imgUrl = r"https://gitee.com/RiskyJR/pic-bed/raw/master/comm-timeline-graphic-1024x380.png"
    image.add(
        src=imgUrl,
        # image align center should modify outside
        style_opts={
            "style": "margin-top: 20px;text-align: center;width:1800px;height:900px;"},
    )
    image.set_global_opts(
        title_opts=ComponentTitleOpts(title="Time Line")
    )
    image.render("../html/imageTest.html")
    print("horizontal line image finished...\n")
    return image


def UpdateTimeLineImage(startTick_x=['2021-08-09 09:00:00', '2021-08-09 09:45:00',
                                     '2021-08-09 11:11:00', '2021-08-09 14:30:00',
                                     '2021-08-09 15:18:00',
                                     '2021-08-09 16:40:00', '2021-08-09 17:19:00'],
                        eventName_x=['开会', '发票', 'visual-code', '舆情分析',
                                     'AOA-Paper', 'AOA-Paper', 'visual-code']):
    colors = ['#E5562D', '#E0A459', '#CFBE65', '#A8CF65', '#6FD67D', '#68D5AE'
              '#6FD0DB', '#5294D0', '#595CD0', '#9E59D0', '#D05994']
    # data preprocession
    # datetime-str→datetime→baseline→gap

    startTick = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
                 for x in startTick_x]
    zeroTick = datetime.strptime(datetime.strftime(
        startTick[1], "%Y-%m-%d")+" 07:00:00")
    stopTick = zeroTick+timedelta(hours=19)
    eventName = eventName_x
    eventLast_x = [30, 78, 33, 47, 69, 39, 15]
    eventLast = eventLast_x
    # startTick_t = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S")
    #                for ii in startTick]
    levels = np.array([-5, 5, -3, 3, -1, 1])
    fig, ax = plt.subplots(figsize=(24, 24*0.618),
                           facecolor='#D6D7C5', dpi=300)

    # Create the base bar from 5am to 1am
    start = datetime.strptime('2021-08-09 05:00:00', '%Y-%m-%d %H:%M:%S')
    stop = datetime.strptime('2021-08-10 02:00:00', '%Y-%m-%d %H:%M:%S')
    baseGapMin = (stop-start).total_seconds()/60
    ax.set(facecolor="#D6D7C5")
    if False:
        ax.broken_barh([(0, baseGapMin)],
                       (-1/2, 1), alpha=.5, facecolors='#ace9e8', edgecolors='white')
    else:
        ax.arrow(0, 0, baseGapMin, 0, width=0.01, length_includes_head=False, head_width=0.25,
                 head_length=25, ec='white')

    ax.set_ylim(-8, 8)
    ax.set_title('Daily Time Line', fontsize=60, color='white')
    for ii, (iname, itick, ieventLast) in enumerate(zip(eventName, startTick, eventLast)):
        barhColor = colors[ii % 4]
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'
        tickTemp = datetime.strptime(itick, "%Y-%m-%d %H:%M:%S")
        curPointX = (tickTemp-start).total_seconds()/60
        curPointX_M = curPointX + ieventLast/2
        ax.scatter(curPointX_M, 0, s=100, facecolor='w',
                   edgecolor=barhColor, zorder=9999)
        # a line up to the text
        ax.plot((curPointX_M, curPointX_M), (0, level), c='white', alpha=.5)
        # text
        itext = iname+"\n"+itick+"|"+str(ieventLast)
        ax.text(curPointX_M, level, itext,
                horizontalalignment='center', verticalalignment=vert, fontsize=20,
                backgroundcolor='#C3EAE9')
        # broken_bar
        ax.broken_barh([(curPointX, ieventLast)], (-1/2, 1),
                       facecolors=barhColor, edgecolors='white', lw=4)
    if False:
        # todo:xlabel setting
        ax.get_xaxis().set_major_locator(
            mdates.MinuteLocator(byminute=range(60), interval=10))
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%H %M"))
        fig.autofmt_xdate()

    # Remove components for a cleaner look
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    plt.setp((ax.get_xticklabels() + ax.get_xticklines() +
              list(ax.spines.values())), visible=False)
    if False:
        imageFile = '../html/pic/timeline.png'
        plt.savefig(imageFile, bbox_inches='tight')
        print('image generated', imageFile)
        return imageFile
    else:
        plt.show()
    print("从眼里留下谢谢两个字 尽管叫我疯子 不准叫我傻子")


if __name__ == "__main__":
    UpdateTimeLineImage()
    # DrawImage()
