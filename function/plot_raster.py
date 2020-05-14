# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:30:00 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

def plot_raster(file_name,store_location):
    y = []
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        for row in reader:
            temp = []
            for item in row:
                temp.append(float(item))
            y.append(temp)
    y = np.array(y)
    y_plot = (1*(y>0)).tolist()
    plt.imshow(y_plot, cmap='Greys')
    plt.savefig(store_location+'/blkwht.png', interpolation='nearest')
    plt.show()