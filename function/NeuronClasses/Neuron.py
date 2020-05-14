# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:14:57 2020

@author: li xiang
"""
#basic neuron
class Neuron:
    def __init__(self,bodyID,name=None,location=None):
        self.bodyID = bodyID
        self.type = 'Normal'
        if name != None:
            self.name = name
        else:
            self.name = 'anonymous'
        if location != None:
            self.location = name
        else:
            self.location = 'anonymous'
        self.tau = lambda x:1 #user can define their own tau function but is NOT RECOMMENDED