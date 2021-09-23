# -*- coding:utf-8 -*-
"""
    根据gatte-test.xlsx中记录的数据生成各种pyehcharts图。
    !important https://blog.csdn.net/u011888840/article/details/105688756
"""
from os import path, listdir, remove

from pyecharts.faker import Faker
from readDataFromExcel import DataFromExcel
import math
from datetime import datetime, date, timedelta
import pandas as pd
from DrawBar import DrawBar
from DrawMap import DrawMap
from DrawLine import DrawLine
from DrawWordCloud import DrawWordCloud
from DrawPie import DrawPie
from GetFlightInfo import FlightInfo
from bs4 import BeautifulSoup
from DrawImage import UpdateTimeLineImage


class TimeCharts():
    def __init__(self, excelFile, *w, **kw):
        self.exlsData = list()
        # 数据文件检查
        # todo:*.xlsx文件后缀检查
        if path.isfile(excelFile):
            self.gatte = excelFile
            df = DataFromExcel(self.gatte)
            self.exlsData = df.getData()
        else:
            self.gatte = "not a exist file"
            print("%s,doesn't exist\n" % (excelFile))

    """
        function:
            获取指定日期(2021-8-1)段内的记录数据
        definition:
            getDateSpecTime(self, startDay: str = "today", endDay: str = "today")
        params:
            startDay,起始日期
            endDay,结束日期
        return:
            pyecharts-Pie
    """

    def getDateSpecTime(self,
                        startDay: str = "today",
                        endDay: str = "today",
                        **kw):
        setTimeStrFormat = '%Y-%m-%d'
        retSegData = pd.DataFrame(columns=['起始', '终止', '事件', '时长', 'other'])
        if startDay == "today":
            startDay_i = datetime.combine(date.today(), datetime.min.time())
        else:
            startDay_i = datetime.strptime(startDay, setTimeStrFormat)

        if endDay == "today":
            endDay_i = datetime.combine(
                date.today(), datetime.min.time()) + timedelta(days=1)
        else:
            endDay_i = datetime.strptime(endDay, setTimeStrFormat)
        curSheet = self.exlsData
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
                        'other': curSheet.iloc[curIndex, 4],
                    },
                    ignore_index=True)
        return retSegData

    """
        function:
                daily pie(根据dateDraw设置参数绘制饼图)
        definition:
                def dailyPie(self,startDay: str = "today", endDay: str = "today")
        params:
                startDay,起始日期
                endDay,结束日期
        return:
                pyecharts-Pie

    """

    def dailyPie(self, startDay: str = "today", endDay: str = "today", **kw):
        try:
            # today
            startDayIn = startDay
            endDayIn = endDay
            dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
            pieData = mergeListToDict(dataDraw['事件'].tolist(),
                                      dataDraw['时长'].tolist())
            titleIn = startDay
            if startDay == "today":
                titleIn = date.today().strftime('%Y-%m-%d')
            # throw out error:ZeroDivisionError: division by zero
            1 / len(pieData)
            return DrawPie(pieData, title=titleIn)
        except:
            return DrawPie(pieData, title=titleIn)

    """
        function:
            绘制一段时间内事件图云(默认为最近一周事件)
        definition:
            periodWordCloud(self)
        params:
            startDay,起始日期
            endDay,结束日期
        return:
            pyecharts-Pie
    """

    def periodWordCloud(self, endDay="today", *k, **kw):
        try:
            endDayIn = endDay
            if endDay == "today":
                endDayIn = date.today().strftime('%Y-%m-%d')
            startDayIn = datetime.strptime(endDayIn,
                                           '%Y-%m-%d') - timedelta(days=7)
            startDayIn = startDayIn.strftime('%Y-%m-%d')
            dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
            word_dict = dict()
            word_mesh = list()
            eventList = dataDraw['事件'].tolist()
            eventStr = str()
            for j in eventList:
                eventStr += str(j) + "-"
            eventSplit = eventStr.split("-")
            for k in eventSplit:
                if k in word_dict.keys():
                    word_dict[k] += 1
                else:
                    word_dict[k] = 1
            for i in word_dict.keys():
                word_mesh.append([i, word_dict[i]])
            # check the list is empty
            1 / len(word_mesh)
        except:
            word_mesh = [("幺鸡", "12"), ("垮", "50"), ("🀍", "7"), ("LOL", "20"),
                         ("🔞", "3"), ("pubg", "15"), ("🤣", "21"), ("杠", "18"),
                         ("🈹", "12"), ("⚅", "7"), ("🤏", "23"), ("蹦子", "18"),
                         ("下棋", "15")]
        return DrawWordCloud(word_mesh, backgroundpic="")

    """
        function:
            绘制一段时间内事件时序图(默认为最近一天事件)
        definition:
            dailyLine(self, day="today")
        params:
            day,日期('%Y-%m-%d')
        return:
            pyecharts-Line
    """

    def dailyLine(self, startDay: str = "today", endDay: str = "today", **kw):
        try:
            startDayIn = startDay
            endDayIn = endDay
            titleIn = startDay
            dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
            startTickList = dataDraw['起始'].tolist()
            if startDay == "today":
                titleIn = date.today().strftime('%Y-%m-%d')
            event_x = list()
            event_y = list()
            for j in startTickList:
                curIndex = startTickList.index(j)
                event_x.append(
                    str(dataDraw.iloc[curIndex, 2]) + '\n' +
                    j.strftime("%H-%M"))
                event_y.append(int(dataDraw.iloc[curIndex, 3]))
            xDataIn = event_x
            yDataIn = event_y
            1 / (len(xDataIn) * len(yDataIn))
        except:
            xDataIn = Faker.choose()
            yDataIn = Faker.values()
            titleIn = "Test Data"
        return DrawLine(xDataIn, yDataIn, title=titleIn)

    """
        function:
            绘制一段时间内事件柱状图(默认为最近一天事件)
        definition:
            dailyBar(self, day="today")
        params:
            day,日期('%Y-%m-%d')
        return:
            pyecharts-Bar
    """

    def dailyBar(self, startDay: str = "today", endDay: str = "today", **kw):
        try:
            startDayIn = startDay
            endDayIn = endDay
            titleIn = startDay
            dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
            startTickList = dataDraw['起始'].tolist()
            if startDay == "today":
                titleIn = date.today().strftime('%Y-%m-%d')
            event_x = list()
            event_y = list()
            for j in startTickList:
                curIndex = startTickList.index(j)
                event_x.append(
                    str(dataDraw.iloc[curIndex, 2]) + '\n' +
                    j.strftime("%H-%M"))
                event_y.append(int(dataDraw.iloc[curIndex, 3]))
            xDataIn = event_x
            yDataIn = event_y
            1 / (len(xDataIn) * len(yDataIn))
        except:
            xDataIn = Faker.choose()
            yDataIn = Faker.values()
            titleIn = "Test Data"
        return DrawBar(xDataIn, yDataIn, title=titleIn)

    """
    函数:
        航班信息
    定义:
        flightMap(self)
    输入:
        updateData,bool
    输出:
        pyecharts,geo
    """

    def flightMap(self, updateData=True, *k, **kw):
        # delte other flight infomation data
        if 'removeFlightData' in kw and kw['removeFlightData']:
            dataRelPath = './/..//data'
            remainData = [
                'FlightDeparture-test.xlsx', 'FlightArrival-test.xlsx',
                'FlightDeparture-' + datetime.now().strftime('%Y-%m-%d') +
                '.xlsx', 'FlightArrival-' +
                datetime.now().strftime('%Y-%m-%d') + '.xlsx'
            ]
            a = listdir(dataRelPath)
            b = path.abspath(dataRelPath)
            for k in a:
                if (not k in remainData) and ('Flight' in k):
                    remove(path.join(b, k))
        # path.listdir()
        if updateData:
            filePostfix = datetime.now().strftime("%Y-%m-%d") + ".xlsx"
            ArrivalFile = "..//data//FlightArrival-" + filePostfix
            DepartureFile = "..//data//FlightDeparture-" + filePostfix
            if not path.isfile(ArrivalFile) or not path.isfile(DepartureFile):
                FlightInfo(ArrivalFile, DepartureFile)
        else:
            ArrivalFile = "..//data//FlightArrival-test.xlsx"
            DepartureFile = "..//data//FlightDeparture-test.xlsx"
        return DrawMap(FlightArrivalFile=ArrivalFile,
                       FlightDepartureFile=DepartureFile)

    """
    函数:
        水平时间线(图)
    定义:
        horizontalLineImage(self)
    输入:
        none
    输出:
        pyecharts,image
    """

    def horizontalLineImage(self,
                            startDay: str = "today",
                            endDay: str = "today",
                            **kw):
        try:
            startDayIn = startDay
            endDayIn = endDay
            dataDraw = self.getDateSpecTime(startDayIn, endDayIn)
            startTickList = dataDraw['起始'].tolist()
            startTickIn = [
                x.strftime("%Y-%m-%d %H:%M:%S") for x in startTickList
            ]
            eventNameIn = [str(y) for y in dataDraw['事件'].tolist()]
            eventLastIn = [int(z) for z in dataDraw['时长'].tolist()]
            1 / len(startTickIn) / len(eventNameIn) / len(eventLastIn)
        except:
            startTickIn = [
                '2021-08-09 09:00:00', '2021-08-09 09:45:00',
                '2021-08-09 11:11:00', '2021-08-09 14:30:00',
                '2021-08-09 15:18:00', '2021-08-09 16:40:00',
                '2021-08-09 17:19:00'
            ]
            eventNameIn = [
                '开会', '发票', 'visual-code', '舆情分析', 'AOA-Paper', 'AOA-Paper',
                'visual-code'
            ]
            eventLastIn = [30, 78, 33, 47, 69, 39, 15]
        UpdateTimeLineImage(startTickIn, eventNameIn, eventLastIn)


"""
    函数:
        将两个list合并为dict，list_name标签列表，list_value值列表
    定义:
        def mergeListToDict(list_name, list_value)
    输入:
        list_name,name(list)
        list_value,value(list)
    输出:
        {'list_name',list_value}
"""


def mergeListToDict(list_name, list_value):
    # 删除nan
    list_name_c = list()
    for i in list_name:
        if isinstance(i, float):
            if not math.isnan(i):
                list_name_c.append(i)
        else:
            list_name_c.append(i)

    list_value_c = [x for x in list_value if not math.isnan(x)]
    mergeDict = dict()
    for k, j in zip(list_name_c, list_value_c):
        if k in list(mergeDict.keys()):
            mergeDict[k] = j + mergeDict[k]
        else:
            mergeDict[k] = j
    return mergeDict


def modifyMainPage(mainpagefile="..//html//mainpage.html"):
    with open(mainpagefile, "r+", encoding='utf-8') as html:
        html_bf = BeautifulSoup(html, 'lxml')
        # 修改网页背景色
        body = html_bf.find("body")
        body["style"] = "background-color:#D6D7C5;"
        # 修改header标签
        header = html_bf.find("header")
        if header is None:
            header = html_bf.new_tag("header")
            html_bf.html.body.insert(1, header)
        header.string = datetime.now().strftime("%Y-%m-%d")
        header["style"] = "background-color:#D6D7C5;font-size:50px;" + \
            "text-align:center;font-family:'Impact';"+"color:#58B4B9;"
        html_new = str(html_bf)
        html.seek(0, 0)
        html.truncate()
        html.write(html_new)
        html.close()


"""
    main page
"""


def mainPage():
    # generate module
    if False:
        Tc_1 = TimeCharts('..//data//gatte-test-1.xlsx')
        Tc_1.dailyPie(startDay="2021-09-22", endDay="2021-09-23")
        Tc_1.periodWordCloud(endDay="2021-09-23")
        Tc_1.dailyLine(startDay="2021-09-22", endDay="2021-09-23")
        Tc_1.dailyBar(startDay="2021-09-22", endDay="2021-09-23")
        Tc_1.flightMap(updateData=True, removeFlightData=True)
        Tc_1.horizontalLineImage(startDay="2021-09-22", endDay="2021-09-22")
        modifyMainPage()
    else:
        Tc_1 = TimeCharts('..//data//gatte-test-1.xlsx')
        Tc_1.dailyPie()
        Tc_1.periodWordCloud()
        Tc_1.dailyLine()
        Tc_1.dailyBar()
        Tc_1.flightMap(updateData=True, removeFlightData=True)
        Tc_1.horizontalLineImage()
        modifyMainPage()


if __name__ == "__main__":
    mainPage()
    print('main page run finished....')