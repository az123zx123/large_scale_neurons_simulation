# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:27:29 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""
import sys
#sys.path.append('C:\\Users\\Song\\Documents\\9. FinalTool\\python version V1\\python version V1\\python version')
sys.path.append('..')
import csv
import numpy as np
import matplotlib.pyplot as plt

from invertconnectome import invertconnectome as invert

from NeuronClasses import Neuron
from NeuronClasses import SpikeAdapt
from NeuronClasses import Bursting

def process(filename,neural_list_filename,Ncluster,NpC,Connectivity,Topology):
    connectome = []
    tau_list = []
    connections = []
    neuronList = []
    
    with open(filename) as connectionFile:
        reader = csv.DictReader(connectionFile)
        for i in reader:
            connections.append(i)
    # print('connections')
    # print(connections)
    for item in connections:
        if item['bodyId_pre'] not in neuronList:
            neuronList.append(item['bodyId_pre'])
    for item in connections:
        if item['bodyId_post'] not in neuronList:
            neuronList.append(item['bodyId_post'])
    # print('neuron list')
    # print(neuronList)
    connectome = np.zeros((len(neuronList), len(neuronList)))
    for item in connections:
        x = neuronList.index(item['bodyId_pre'])
        y = neuronList.index(item['bodyId_post'])
        weight = item['weight']
        connectome[x,y] = weight

    with open(neural_list_filename) as neuronFile:
        reader = csv.DictReader(neuronFile)
        for row in reader:
            if row['type'] == 'Neuron':
                tau_list.append((Neuron.Neuron(int(row['bodyId']))).tau)
            elif row['type'] == 'SpikeAdapt':
                tau_list.append((SpikeAdapt.SpikeAdapt(int(row['bodyId']))).tau)
            elif row['type'] == 'Bursting':
                tau_list.append((Bursting.Bursting(int(row['bodyId']))).tau)

    # print('connectome')
    # print(connectome)

    # print('tau_list')
    # print(self.tau_list)

    Q = invert(connectome, Ncluster, NpC, Connectivity, Topology)
    # numpy.savetxt("invertMat.csv", Q, delimiter=",")
    # Q = np.linalg.inv(connectome)

    return Q, tau_list, len(neuronList)

    
        
            
        