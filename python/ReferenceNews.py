# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:51:15 2021

@author: W-H
"""

import requests


class RefNews():
    BaseUrl = r"http://www.jdqu.com/"

    def __init__(self):
        super().__init__()
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31'}
        html = requests.get(self.BaseUrl, headers=headers)
        if html.status_code == 200:
            print(html.text)
        else:
            print(html.status_code)

    def _NonoFunc(self):
        pass


if __name__ == "__main__":
    Rn = RefNews()
