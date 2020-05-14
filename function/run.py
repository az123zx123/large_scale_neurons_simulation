# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:27:29 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""
import sys
sys.path.append('C:\\Users\\Song\\Documents\\9. FinalTool\\python version V1\\python version V1\\python version')
import numpy as np
from snnFunc import snnFunc

def run(Q, tau_list, nIter):
    y_init = -0.3*np.ones([len(tau_list)])
    y = snnFunc(Q,tau_list,nIter,y_init)
    print('Run finished, outputing y')
    return y

    
        
            
        