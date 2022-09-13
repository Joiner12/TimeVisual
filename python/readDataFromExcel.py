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

    def __init__(self, exlsFile, updateData=True, *w, **kw):
        # 数据文件检查
        self.exlsFile = exlsFile
        if not path.isfile(self.exlsFile):
            print("读取 "+self.exlsFile+" 数据**失败**...\n")
            return
        if updateData:
            self._updateDailyData(exlsFile)

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
    """
    函数:
        将原始记数据最新一张excel表单拷贝到目标excel中,更新每日记录。文档只保存两张表单，按照FIFO原则操作。
    定义:
        updateDailyData(srcfile, tarfile, *k, **kw)
    参数:
        srcfile,源文件绝对路径
        tarfile,目标文件绝对路径
    输出:
        none
    """

    def _updateDailyData(self, srcfile=r"E:\Notes\gatte.xlsx", *k, **kw):
        if not path.isfile(srcfile):
            print("srcfile load failed :"+srcfile)
            return
        tarfile = self.exlsFile
        srcexls = pd.ExcelFile(srcfile)
        tarexls = pd.ExcelWriter(tarfile)
        srcIndex = srcexls.sheet_names[-3:-1]
        for k in srcIndex:
            srcexls.parse(k).to_excel(tarexls,sheet_name=k,index=False)
        tarexls.save()
        print("updated daily data...")


if __name__ == "__main__":
    df = DataFromExcel(r"..//data//gatte-test-1.xlsx")
    # exlsData = df.getData()
    # print(exlsData)
