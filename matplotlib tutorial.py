"""
Author: Aldiana Kucevic
Date: 25-12-2022
Function: Matplotlib oefening
"""

# code voor simpele diagrammen:

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2, 4, 7, 4, 0, 6, 5, 3, 5, 20]
# plt.xlabel = ("frequentie")
# plt.ylabel = ("waardes")
# plt.title = ("Hoe vaak komt dit voor?")
# plt.plot(x, y) # hier bepaal je welke diagram je wilt
# plt.show()


# code voor piechart:
# fig, ax = plt.subplots()
# y = np.array([35, 25, 25, 15])
# x = ["Apples", "Bananas", "Cherries", "Strawberries"]
# plt.pie(y, labels=x) # werkt niet zonder labels=
# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles, labels)
# ax.legend(bbox_to_anchor=(1, 1),bbox_transform=fig.transFigure)
# plt.show()

# code legenda

from matplotlib.legend_handler import HandlerLine2D

fig, ax = plt.subplots()
line1, = ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], marker='o', label='Line 1')
line2, = ax.plot([2, 4, 7, 4, 0, 6, 5, 3, 5, 20], marker='o', label='Line 2')

ax.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.show()