# -*- coding:utf-8 -*-
"""
    功能：
         读取Excel文本中的时间、事件等数据到标准数据
"""

import pandas as pd
from os import path


class DataFromExcel():
    exlsData = list()  # excel读取的数据
    rootPath = ""

    def __init__(self, exlsFile):
        self.exlsData = "像花虽未红 如冰虽不冻\n"
        self.rootPath = path.dirname(path.dirname(__file__))
        if not path.isfile(exlsFile):
            return
        self.exlsData = pd.read_excel(exlsFile, sheet_name=None)
        print("读取 "+exlsFile+" 数据...\n")

    def getData(self):
        return self.exlsData


if __name__ == "__main__":
    df = DataFromExcel(r"..//data//gatte-test.xlsx")
    exlsData = df.getData()
    print(exlsData)
