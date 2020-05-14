# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:35:31 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""

import numpy as np
import csv

neuronCount = 10

neuron_list = []
for i in range(neuronCount):
    neuron_list.append([i,0,'Neuron'])
with open('C:\\Users\\Song\\Documents\\9. FinalTool\\python version V1\\python version V1\\python version\\demo\\neuron_list.csv','w',newline='') as neuron:
    writer = csv.writer(neuron)
    writer.writerow(['bodyId','location','type'])
    for row in neuron_list:
        writer.writerow(row)

connectivity_list = []
for i in range(neuronCount):
    connectivity_list.append([i,neuronCount-i-1,1])
with open('C:\\Users\\Song\\Documents\\9. FinalTool\\python version V1\\python version V1\\python version\\demo\\connectivity_list.csv','w',newline='') as connectivity:
    writer = csv.writer(connectivity)
    writer.writerow(['bodyId_pre','bodyId_post','weight'])
    for row in connectivity_list:
        writer.writerow(row)