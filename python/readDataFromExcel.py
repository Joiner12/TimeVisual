# -*- coding:utf-8 -*-
"""
    功能：
         读取Excel文本中的时间、事件等数据到标准数据
"""

import pandas as pd
from os import path


class DataFromExcel():
    exlsData = list()  # excel读取的数据
    exlsFile = str()
    rootPath = ""

    def __init__(self, exlsFile, *w, **kw):
        # 数据文件检查
        self.exlsFile = exlsFile
        if not path.isfile(self.exlsFile):
            print("读取 "+self.exlsFile+" 数据**失败**...\n")
            return

    def getData(self, meansSelector=0):
        if meansSelector == 0:
            excelfile = pd.ExcelFile(self.exlsFile)
            exceldata = list()
            for k in excelfile.sheet_names:
                exceldata.append(pd.read_excel(excelfile, sheet_name=k))
            self.exlsData = pd.concat(exceldata, ignore_index=True)
            print("读取 "+self.exlsFile+" 数据**完成**...\n")
        elif meansSelector == 1:
            self.exlsData = pd.read_excel(self.exlsFile)
        else:
            print("感情就是这样 怎么一不小心太疯狂")
        return self.exlsData


if __name__ == "__main__":
    df = DataFromExcel(r"..//data//gatte-test.xlsx")
    exlsData = df.getData()
    print(exlsData)
