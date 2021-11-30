# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:33:06 2021

@author: W-H
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 11

# 导入一些要玩的数据
iris = datasets.load_iris()
x = iris.data[:, :2]  # 我们只采用前两个feature,方便画图在二维平面显示
y = iris.target

h = .02  # 网格中的步长

# 创建彩色的图
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# weights是KNN模型中的一个参数，上述参数介绍中有介绍，这里绘制两种权重参数下KNN的效果图
for weights in ['uniform']:
    # for weights in ['uniform', 'distance']:
    # 创建了一个knn分类器的实例，并拟合数据
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(x, y)

    # 绘制决策边界，为此，我们将为每个分配一个颜色
    # 来绘制网格中的点 [x_min, x_max]x[y_min, y_max].
    x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 将结果放入一个彩色图中
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # 绘制训练点
    plt.scatter(x[:, 0], x[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')" %
              (n_neighbors, weights))

# plt.show()
