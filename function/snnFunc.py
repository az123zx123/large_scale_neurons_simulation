# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:33:18 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""

import numpy as np

def snnFunc(Q, neural_list_tau, nIter, yInit):
    Q = Q.todense()
    nNeurons = len(neural_list_tau)
    y = np.zeros((nNeurons,nIter))
    thr = 0.0 # Spike threshold
    l = 12*np.ones((nNeurons,1)) # Convergence hyperparameters
    Vi = -0.5*np.ones((nNeurons,1)) #membrane potential
    y[:,0] = yInit #inital y
    bi = 0.03*np.random.random((nNeurons,1)) #External stimuli current
    C = 0.5 #Regularization hyper-parameter
    print('SNN iteration begins')
    for t in range(nIter):
        ind = Vi > thr
        Vi[ind] = thr
        psi = C*(ind)
        G = -np.transpose(Q)@Vi - bi + psi
        G = G.reshape((nNeurons,1))
        Vi = (-G+np.multiply(l, Vi))/(-np.multiply(Vi,G)+l) - Vi
        for i in range(nNeurons):
            Vi[i] += Vi[i]/(neural_list_tau[i](t))
        y[:,t] =  (Vi + psi).reshape(nNeurons)
    print('SNN iteration ends')
    return y
    
    