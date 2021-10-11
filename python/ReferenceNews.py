# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:51:15 2021

@author: W-H
"""

import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import re
import os


class RefNews():
    BaseUrl = r"http://www.jdqu.com"
    html = 0
    picDir = ''
    filePath = ''
    htmlFile = ''
    pageDate = ''

    def __init__(self, *pk, **pkw):
        super().__init__()
        # change workspace into script dir
        self.filePath = os.path.split(os.path.abspath(__file__))[0]
        os.chdir(self.filePath)
        # get base web
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
        }
        self.html = requests.get(self.BaseUrl, headers=self.headers)
        if not self.html.status_code == 200:
            return
        else:
            print('Request From:', self.BaseUrl, 'Success')
        todayRnsLink = self._GetPaperLink()
        validSubUrls = self._ParseValidPageUrl(
            todayRnsLink[0], todayRnsLink[1])
        if not validSubUrls is None:
            self._DownLoadPagePicture(validSubUrls)

    def _GetPaperLink(self, *pk, **pkw):
        newspaper = dict()
        self.html.encoding = self.html.apparent_encoding
        htmlBs = BeautifulSoup(self.html.text, "lxml")
        ref = htmlBs.select('.img-wrap a')
        for j in ref:
            papertitle = j.get("title")
            paperLink = self.BaseUrl + j.get("href")
            # print(papertitle, paperLink)
            newspaper[papertitle] = paperLink
        # todo:filter newspaper by date and name
        todayReferenceNewsLink = list(newspaper.values())
        todayReferenceNewsLink = todayReferenceNewsLink[0]
        todayReferenceNewsName = list(newspaper.keys())
        todayReferenceNewsName = todayReferenceNewsName[0].replace(
            '点击阅读 ', '')
        # print(todayReferenceNewsName[0])
        return (todayReferenceNewsName, todayReferenceNewsLink)

    def _ParseValidPageUrl(self, papername="", paperbaselink="", *pk, **pkw):
        name = papername
        mat = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", name)
        self.pageDate = mat[0]
        # folder to save picture
        if datetime.strptime(self.pageDate, '%Y-%m-%d').date() == date.today():
            print("Today News", papername)
        else:
            print("Yesterday Flower", papername)

        # check for valid picture page url
        subUrl = paperbaselink.replace('.html', '')
        validPageLinks = list()
        try:
            pageCounter = 0
            while True:
                pageCounter += 1
                testUrl = subUrl+'-'+str(pageCounter)+'.html'
                html = requests.get(testUrl, headers=self.headers)

                if not html.status_code == 200 or pageCounter > 40:
                    break
                validPageLinks.append(testUrl)
        except:
            print('page is not accessible')
            return
        return validPageLinks

    def _DownLoadPagePicture(self, urls=[], *pk, **pkw):
        # picture folder
        self.picDir = os.path.join(self.filePath, 'NewsPic')
        if not os.path.isdir(self.picDir):
            os.mkdir(self.picDir)
        self.picDir = os.path.join(self.picDir, self.pageDate)
        # specific day's folder
        if not os.path.isdir(self.picDir):
            os.mkdir(self.picDir)
        for url in urls:
            html = requests.get(url, headers=self.headers)
            html.encoding = html.apparent_encoding
            htmlBs = BeautifulSoup(html.text, "lxml")
            imgHtml = htmlBs.select('img')
            # imgName = imgHtml[0].get('alt')
            imgUrl = imgHtml[0].get('src')
            curPic = os.path.join(self.picDir, imgUrl.split('/')[-1])
            # print(curPic)

            r = requests.get(imgUrl)
            with open(curPic, "wb")as f:
                f.write(r.content)
                f.close()
            i = urls.index(url)
            print('\rLoading：{0}{1}%'.format(
                '▉'*(i+1), ((i+1)*100/len(urls))), end='')

    def _WriteHtml(self, *pw, **pkw):
        self.htmlFile = os.path.join(
            self.picDir, 'ReferenceNews'+self.pageDate+'.html')
        print(self.htmlFile)


if __name__ == "__main__":
    Rn = RefNews()
