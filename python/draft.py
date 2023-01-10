# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:34:46 2021

@author: W-H
"""

import matplotlib.pyplot as plt
import numpy as np

rssi = [
    -63.08, -66.88, -69.10, -70.68, -71.91, -72.91, -73.75, -74.48, -75.13,
    -75.71, -76.23, -76.71, -77.15, -77.55, -77.93, -78.27
]

dist = [
    0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5,
    8.0
]
plt.plot(dist,
         rssi,
         color='green',
         marker='o',
         linestyle='dashed',
         linewidth=2,
         markersize=12)
plt.show()

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

#%%
# fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))
fig, ax = plt.subplots()
size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
# Normalize vals to 2 pi
valsnorm = vals / np.sum(vals) * 2 * np.pi
# Obtain the ordinates of the bar edges
valsleft = np.cumsum(np.append(0, valsnorm.flatten()[:-1])).reshape(vals.shape)

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3) * 4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.bar(x=valsleft[:, 0],
       width=valsnorm.sum(axis=1),
       bottom=1 - size,
       height=size,
       color=outer_colors,
       edgecolor='w',
       linewidth=1,
       align="edge")

# ax.bar(x=valsleft.flatten(),
#        width=valsnorm.flatten(),
#        bottom=1 - 2 * size,
#        height=size,
#        color=inner_colors,
#        edgecolor='w',
#        linewidth=1,
#        align="edge")

ax.annotate("", xy=(0, 1), xytext=(0, 0.7), arrowprops=dict(arrowstyle="->"))
ax.set(title="Pie plot with `ax.bar` and polar coordinates")
ax.set_axis_off()
plt.show()
#%%
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = [
    "225 g flour", "90 g sugar", "1 egg", "60 g butter", "100 ml milk",
    "1/2 package of yeast"
]

data = [225, 90, 50, 60, 100, 5]

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props,
          zorder=0,
          va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i],
                xy=(x, y),
                xytext=(1.35 * np.sign(x), 1.4 * y),
                horizontalalignment=horizontalalignment,
                **kw)

ax.set_title("Matplotlib bakery: A donut")

plt.show()

#%% 
import re
a = " 全部待办 14"
b = re.split(r' ', a)
print("全部" in a)