# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:34:46 2021

@author: W-H
"""

import matplotlib.pyplot as plt
import numpy as np
rssi = [-63.08, -66.88, -69.10, -70.68, -71.91,
        -72.91, -73.75, -74.48, -75.13, -75.71,
        -76.23, -76.71, -77.15, -77.55, -77.93,
        -78.27]

dist = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5,
        4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
plt.plot(dist, rssi, color='green', marker='o',
         linestyle='dashed',  linewidth=2, markersize=12)
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