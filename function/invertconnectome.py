# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:45:23 2020

@author: li xiang
"""

import numpy as np
from scipy.sparse import block_diag
from scipy.sparse import random
from scipy import sparse
from scipy.sparse.linalg import norm
import numpy.matlib

def invertconnectome(W, Ncluster, NpC, Connectivity, Topology):
    # Mask Matrix
    cluster = np.random.rand(NpC,NpC)
    ConCell = []
    for i in range(Ncluster):
        ConCell.append(cluster)
    BigCon = block_diag(ConCell)
    BigCon = BigCon.todense()
    chipDensity = Connectivity/NpC # interconnecting neuron densities
    # 1D
    if Topology == 1:
        for i in range(Ncluster-1):
            BigCon[(i+1)*NpC:(i+2)*NpC,i*NpC:(i+1)*NpC] = random(NpC, NpC, chipDensity).toarray()
            BigCon[i*NpC:(i+1)*NpC,(i+1)*NpC:(i+2)*NpC] = random(NpC, NpC, chipDensity).toarray()
    # 2D
    if Topology == 2:
        for i in range(Ncluster - 1):
                    BigCon[(i+1)*NpC:(i+2)*NpC,i*NpC:(i+1)*NpC] = random(NpC,NpC,chipDensity).toarray()
                    BigCon[i*NpC:(i+1)*NpC,(i+1)*NpC:(i+2)*NpC] = random(NpC,NpC,chipDensity).toarray()
        for i in range(Ncluster - 2):
                    BigCon[(i+1)*NpC:,i*NpC:(i+1)*NpC] = random((int(Ncluster)-i-1)*NpC,NpC,chipDensity).toarray()
                    BigCon[i*NpC:(i+1)*NpC,(i+1)*NpC:] = random(NpC,(int(Ncluster)-i-1)*NpC,chipDensity).toarray()
    M = sparse.csc_matrix(1*(BigCon>0)) #convert mask to sparse matrix
    constraints = (-1, 1)  #user definable 
    nIter = 10 #user definable
    stepSize = 0.05/np.sqrt(nIter) #user definable, constant stepSize is NOT RECOMMENDED
    W = sparse.csc_matrix(W)
    objVals = np.zeros([nIter, 1])
    I = sparse.eye(NpC*Ncluster,format='csc')
    Q = sparse.eye(NpC*Ncluster,format='csc')
    print(W.shape)
    print(I.shape)
    print(Q.shape)
    for i in range(nIter):
        Q += stepSize * (np.transpose(W)@(I-W@Q))
        Q = Q.multiply(M)
        Q[Q<constraints[0]] = constraints[0]
        Q[Q>constraints[1]] = constraints[1]
        objVals[i] = (norm(I - W@Q))**2
        print('step: '+str(i)+' objective: '+str(objVals[i]))
    return Q