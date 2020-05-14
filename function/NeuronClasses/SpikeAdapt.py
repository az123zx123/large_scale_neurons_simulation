# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:08:56 2020

@author: li xiang
"""
import sys
sys.path.append('..')
from NeuronClasses import Neuron
from math import log

class SpikeAdapt(Neuron.Neuron):
    def __init__(self,index,adapt_constant=100,name=None,location=None):
        Neuron.__init__(self,index,name,location)
        self.type = 'SpikeAdapt'
        self.adapt_constant = adapt_constant
        self.tau = lambda x:log(x%self.adapt_constant+2) ##user can define their own tau function under tau function requirement 
    
    