# -*- coding:utf-8 -*-
"""
    获取双流机场进出港航班信息
    http://www.cdairport.com/flightInfor.aspx?t=4
    Reference:
    1.https://zhuanlan.zhihu.com/p/394268763
    2.https://www.cnblogs.com/sanduzxcvbnm/p/10250222.html
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


class FlightInfo():
    arrivalUlrHead = r"http://www.cdairport.com/flightInfor.aspx?t=4&attribute=A&time=0&page="
    departureUrlHead = r"http://www.cdairport.com/flightInfor.aspx?t=4&attribute=D&time=0&page="
    htmlSelector = 'table'
    FlightInfoData = {'Arrival': None, 'Departure': None}

    def __init__(self, arrivalFile: str = "", departureFile: str = ""):
        super().__init__()
        # check flight info
        self._getArrivalInfo(arrivalFile)
        self._getDepartureInfo(departureFile)
        print("get flight info runs finished...\n")

    def _getArrivalInfo(self, savefile=""):
        arrivaldata = getTableFromUrl(
            self.arrivalUlrHead, self.htmlSelector)
        self.FlightInfoData['Arrial'] = arrivaldata
        if not savefile == "":
            arrivaldata.to_excel(savefile)
        print("get flight info of arrival...\n")

    def _getDepartureInfo(self, savefile=""):
        departureData = getTableFromUrl(
            self.departureUrlHead, self.htmlSelector)
        self.FlightInfoData['Departure'] = departureData
        if not savefile == "":
            departureData.to_excel(savefile)
        print("get flight info of departure...\n")

    def GetFlightData(self):
        return self.FlightInfoData


def getTableFromUrl(urlhead, selector):
    FlightInfo = pd.DataFrame()
    for k in range(1, 100, 1):
        url = urlhead+str(k)
        html = requests.get(url)
        # check html status
        if not html.status_code == 200:
            break
        soup = BeautifulSoup(html.text, "lxml")
        # 'table[class="arlineta departab"]'

        tab = soup.select(selector)[0]
        curPage = pd.read_html(tab.prettify(), header=0)[0]
        if not curPage.empty:
            FlightInfo = pd.concat([FlightInfo, curPage])
        else:
            break
    # print(FlightInfo)
    return FlightInfo


if __name__ == "__main__":
    filePostfix = datetime.now().strftime("%Y-%m-%d")+".xlsx"
    arrivalFile = "..//data//FlightArrival-"+filePostfix
    departureFile = "..//data//FlightDeparture-"+filePostfix
    F1 = FlightInfo(arrivalFile, departureFile)
