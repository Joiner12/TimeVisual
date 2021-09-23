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
from datetime import datetime, timedelta

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False


def DrawImage(imgUrl="../html/pic/horizontalLine.png", **kw):
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
                                     'AOA-Paper', 'AOA-Paper', 'visual-code'],
                        eventLast_x=[30, 78, 33, 47, 69, 39, 15], *k, **kw):
    colors = ['#E5562D', '#E0A459', '#CFBE65', '#A8CF65', '#6FD67D', '#68D5AE'
              '#6FD0DB', '#5294D0', '#595CD0', '#9E59D0', '#D05994']
    # datetime-str→datetime→baseline→gap
    # Create the base bar from 5am to 1am
    startTick_t = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
                   for x in startTick_x]
    zeroTick_t = datetime.strptime(datetime.strftime(
        startTick_t[1], "%Y-%m-%d")+" 05:00:00", "%Y-%m-%d %H:%M:%S")
    endTick_t = zeroTick_t+timedelta(hours=19)
    eventName = eventName_x
    eventLast = eventLast_x
    levels = np.array([-5, 5, -3, 3, -1, 1])
    fig, ax = plt.subplots(figsize=(36, 36*0.5625),
                           facecolor='#D6D7C5', dpi=500)
    baseGapMin = (endTick_t-zeroTick_t).total_seconds()/60
    ax.set(facecolor="#D6D7C5")
    ax.broken_barh(
        [(0, baseGapMin)], (-1/2, 1), alpha=.5,
        facecolors='#ace9e8', edgecolors='white', lw=4, capstyle='round')

    ax.set_ylim(-8, 8)
    # set as page background image no need title
    # ax.set_title('Daily Time Line', fontsize=60, color='white')
    for ii, (iname, itick, ieventLast) in enumerate(zip(eventName, startTick_t, eventLast)):
        barhColor = colors[ii % 4]
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'
        # tickTemp = datetime.strptime(itick, "%Y-%m-%d %H:%M:%S")
        curPointX = (itick-zeroTick_t).total_seconds()/60
        curPointX_M = curPointX + ieventLast/2
        ax.scatter(curPointX_M, 0, s=100, facecolor='w',
                   edgecolor=barhColor, zorder=9999)
        # a line up to the text
        ax.plot((curPointX_M, curPointX_M), (0, level), c='white', alpha=.5)
        # text
        itickStr = datetime.strftime(itick, "%m-%d %H:%M")
        itext = iname+"\n"+itickStr+"|"+str(ieventLast)
        textInstance = ax.text(
            curPointX_M, level, itext,
            horizontalalignment='center', verticalalignment=vert, fontsize=20,
            fontfamily='Microsoft YaHei')
        textInstance.set_bbox(
            dict(boxstyle="round", alpha=0.5, color='#C3EAE9'))
        # broken_bar
        ax.broken_barh([(curPointX, ieventLast)], (-1/2, 1),
                       facecolors=barhColor, edgecolors='white', lw=4)

    # Remove components for a cleaner look
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    plt.setp((ax.get_xticklabels() + ax.get_xticklines() +
              list(ax.spines.values())), visible=False)
    plt.xlabel(startTick_t[int(len(startTick_t)/2)].strftime("%Y-%m-%d")+' Time Line',
               loc='left', fontsize=30, fontfamily='Microsoft YaHei', color='white')
    plt.ylabel('Update:'+datetime.now().strftime("%Y-%m-%d"),
               loc='bottom', fontsize=30, fontfamily='Microsoft YaHei', color='white')
    if True:
        imageFile = r'../html/pic/timeline.jpg'
        plt.savefig(imageFile,dpi=400, bbox_inches='tight')
        print('image generated', imageFile)
        return imageFile
    else:
        plt.show()


if __name__ == "__main__":
    UpdateTimeLineImage()
    # DrawImage()
