# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 09:19:05 2021

@author: Peace4Lv
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False 
def test():
    colors = ['yellow', 'green', 'blue', 'red']
    # A list of Matplotlib releases and their dates
    # Taken from https://api.github.com/repos/matplotlib/matplotlib/releases
    startTick = ['2021-08-09 09:00:00', '2021-08-09 09:45:00',
                 '2021-08-09 11:11:00', '2021-08-09 14:30:00', '2021-08-09 15:18:00',
                 '2021-08-09 16:40:00', '2021-08-09 17:19:00']
    endTick = ['2021-08-09 09:30:00', '2021-08-09 11:03:00', '2021-08-09 11:44:00',
               '2021-08-09 15:18:00', '2021-08-09 16:27:00', '2021-08-09 17:19:00',
               '2021-08-09 17:35:00']
    eventName = ['开会', '发票', 'visual-code', '舆情分析',
                 'AOA-Paper', 'AOA-Paper', 'visual-code']
    eventLast = [30, 78, 33, 47, 69, 39, 15]
    startTick_t = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S")
                   for ii in startTick]
    endTick_t = [datetime.strptime(ii, "%Y-%m-%d %H:%M:%S") for ii in endTick]
    levels = np.array([-5, 5, -3, 3, -1, 1])
    fig, ax = plt.subplots(figsize=(24, 24*0.618), facecolor='#D6D7C5',dpi=600)

    # Create the base bar from 5am to 1am
    start = datetime.strptime('2021-08-09 05:00:00', '%Y-%m-%d %H:%M:%S')
    stop = datetime.strptime('2021-08-10 02:00:00', '%Y-%m-%d %H:%M:%S')
    baseGapMin = (stop-start).total_seconds()/60
    ax.set(facecolor="#D6D7C5")
    ax.broken_barh([(0, baseGapMin)],
                   (-1/2, 1), alpha=.5, facecolors='#ace9e8', edgecolors='white')

    ax.set_ylim(-8, 8)
    for ii, (iname, itick, ieventLast) in enumerate(zip(eventName, startTick_t, eventLast)):
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'
        curPointX = (itick-start).total_seconds()/60
        curPointX_M = curPointX + ieventLast/2
        ax.scatter(curPointX_M, 0, s=100, facecolor='w',
                   edgecolor='k', zorder=9999)
        # a line up to the text
        ax.plot((curPointX_M, curPointX_M), (0, level), c='r', alpha=.7)
        # text
        ax.text(curPointX_M, level, iname,
                horizontalalignment='right', verticalalignment=vert, fontsize=14,
                backgroundcolor=(1., 1., 1., .3))
        # broken_bar
        ax.broken_barh([(curPointX, ieventLast)], (-1/2, 1),
                       facecolors=(colors[ii % 4]), edgecolors=('red'))
    # Set the xticks formatting
    # format xaxis with 3 month intervals
    # todo:modify xaxis labels
    if False:
        ax.get_xaxis().set_major_locator(mdates.MinuteLocator(interval=30))
        ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
        fig.autofmt_xdate()

    # Remove components for a cleaner look
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    plt.show()


def test_1():
    fig, ax = plt.subplots(figsize=(24, 24*0.62), facecolor='#D6D7C5', dpi=600)
    ax.set(facecolor="#D6D7C5")
    # ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='blue')
    ax.broken_barh([(10, 50), (60, 40), (100, 20), (120, 10), (130, 10)], (10, 2),
                   facecolors=('red', 'white', 'yellow', 'white', 'green'),
                   edgecolors=('red'))
    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_yticks([15, 25])
    # ax.set_yticklabels('Bill')
    ax.grid(False)
    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    plt.show()


if __name__ == "__main__":
    # test_1()
    test()
