# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:26:35 2020

@author: li xiang
"""
from NeuronClasses import Neuron
class Bursting(Neuron.Neuron):
    def __init__(self,index,bursting_frequency=5,name=None,location=None):
        Neuron.__init__(self,index,name,location)
        self.type = 'Bursting'
        self.bursting_frequency = bursting_frequency
        self.tau = lambda x:int(x/self.bursting_frequency)%2+0.5 #user can define their own tau function under tau function requirement 
    