# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:51:15 2021

@author: W-H
"""

import requests
from bs4 import BeautifulSoup


class RefNews():
    BaseUrl = r"http://www.jdqu.com/"
    html = 0

    def __init__(self, *pk, **pkw):
        super().__init__()
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'
        }
        self.html = requests.get(self.BaseUrl, headers=headers)
        print('Request From:', self.BaseUrl)
        if not self.html.status_code == 200:
            print('Failed,status code:', self.html.status_code)
            return
        else:
            print('Success')
        todayRnsLink = self._GetPaperLink()
        print(todayRnsLink)

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
        todayReferenceNewsName = list(newspaper.keys())
        # print(todayReferenceNewsName[0], todayReferenceNewsLink[0])
        return todayReferenceNewsLink[0]

    def _GetReferencePaper(self, *pk, **pkw):
        pass


if __name__ == "__main__":
    Rn = RefNews()
