# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:41:46 2021

@author: W-H
"""

"""
    1.原始数据格式:
        时间        代码    基金
        2021-09-30  00002  A B C D 
    2.原始数据构造为list格式
    如：[['2020-06', '00002', ('A', 'B', 'C', 'D')],
                ['2020-07', '00002', ('H', 'F', 'N')],
                ['2020-08', '00002', ('M', 'C', 'B', 'X')],
                ['2020-09', '00006', ('Q', 'Z', 'A', 'D')],
                ['2020-10', '00006', ('W', 'P', 'H', 'N')]
                ]
    3.构造关系图

"""




import numpy as np
def createGraph(param1):
    # 生成节点list
    nodes = list()
    edgeTemp = list()
    for k in param1:
        curNodes = k[2]
        edgeTemp.append(curNodes)
        for node in curNodes:
            if not node in nodes:
                nodes.append(node)
    # 生成邻接矩阵(edge)
    edge = np.zeros((len(nodes), len(nodes)), dtype=int)

    # 遍历原始数据 填充邻接矩阵
    for j in edgeTemp:
        for k_1 in j:
            rowIndex = nodes.index(k_1)
            for k_2 in j:
                if not k_2 == k_1:
                    colIndex = nodes.index(k_2)
                    edge[rowIndex, colIndex] += 1
    return {'node': nodes, 'edges': edge}


if __name__ == "__main__":
    testData = [['2020-06', '00002', ('A', 'B', 'C', 'D')],
                ['2020-07', '00002', ('H', 'F', 'N')],
                ['2020-08', '00002', ('M', 'C', 'B', 'X')],
                ['2020-09', '00006', ('Q', 'Z', 'A', 'D')],
                ['2020-10', '00006', ('W', 'P', 'H', 'N')]
                ]

    createGraph(testData)
