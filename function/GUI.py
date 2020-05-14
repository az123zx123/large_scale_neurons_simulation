# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:23:35 2020
Modified on Sat May 9th 2020

@author: li xiang, Song Mo
"""

import tkinter as tk
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox as mb
import numpy as np
import matplotlib.pyplot as plt
import run
import process
import plot_raster
import csv


class Simulator:
    def __init__(self, master):
        self.master = master
        master.title('GT Neuron Spiking Activity Simulator')
        master.geometry('500x300')

        # Variable initialization
        self.filename = ''
        self.neural_list_filename = ''
        self.filename_output = ''
        self.invConnectome = []
        self.tau_list = []
        self.neuronCount = 0

        self.x_baseline = 10
        self.y_baseline = 70

        # Introduction label
        self.sim_note = tk.Label(window,text='Enter parameters value on the left, select files and output path.')
        self.sim_note.place(x=10, y=10)
        self.sim_info = tk.Label(window,text='For information about setting up parameters, click help.')
        self.sim_info.place(x=10, y=27)

        # Funcional buttons
        self.select_mat = tk.Button(window,text='Select Connectivity', command = self.select_connectome, width=15)
        self.select_mat.place(x=self.x_baseline*20, y=self.y_baseline)
        
        self.select_list = tk.Button(window,text='Select Neuron List', command = self.select_list, width=15)
        self.select_list.place(x=self.x_baseline*20, y=self.y_baseline+50)

        self.output = tk.Button(window,text='Set Output Path', command = self.select_output, width=15)
        self.output.place(x=self.x_baseline*20, y=self.y_baseline+100)

        self.process = tk.Button(window,text='Process', command = self.data_process, width=15)
        self.process.place(x=self.x_baseline*20, y=self.y_baseline+150)

        self.run_button = tk.Button(window,text='Run', command = self.run_sim, width=15)
        self.run_button.place(x=self.x_baseline*20+170, y=self.y_baseline+100)

        self.plot = tk.Button(window, text='raster plot', command = self.plot, width=15)
        self.plot.place(x=self.x_baseline*20+170, y=self.y_baseline+150)

        # Spiking time range
        self.spkt = tk.StringVar(window,value='1')
        self.spkt_L = tk.Label(window,text='Spiking Time')
        self.spkt_E = tk.Entry(window, bd =5, width=5)
        self.spkt_E.insert(END, '100')
        self.spkt_L.place(x=self.x_baseline*20+170, y=self.y_baseline+50)
        self.spkt_E.place(x=self.x_baseline*20+250, y=self.y_baseline+50)

        # Number of clusters
        self.nc = tk.StringVar(window, value='1')
        self.L1 = tk.Label(window,text='Ncluster')
        self.E1 = tk.Entry(window, bd =5, width=5)
        self.L1.place(x=self.x_baseline, y=self.y_baseline)
        self.E1.place(x=self.x_baseline*10, y=self.y_baseline)

        # Number per cluster
        self.npc = tk.StringVar(window,value='2')
        self.L2 = tk.Label(window,text='NpC')
        self.E2 = tk.Entry(window, bd =5, width=5)
        self.L2.place(x=self.x_baseline, y=self.y_baseline+50)
        self.E2.place(x=self.x_baseline*10, y=self.y_baseline+50)

        # Connectivity
        self.c = tk.StringVar(window,value='1')
        self.L3 = tk.Label(window,text='Connectivity')
        self.E3 = tk.Entry(window, bd =5, width=5)
        self.L3.place(x=self.x_baseline, y=self.y_baseline+100)
        self.E3.place(x=self.x_baseline*10, y=self.y_baseline+100)

        # Topology
        self.to = tk.StringVar(window, value='2')
        self.L4 = tk.Label(window,text='Topology')
        self.E4 = tk.Entry(window, bd =5, width=5)
        self.L4.place(x=self.x_baseline, y=self.y_baseline+150)
        self.E4.place(x=self.x_baseline*10, y=self.y_baseline+150)

        # Help information and version #
        self.sim_name = tk.Label(window,text='Version 2.0')
        self.sim_name.place(x=425, y=280)
        self.help = tk.Button(window,text='Help', command = self.help, width=10)
        self.help.place(x=10, y=270)

    def select_connectome(self):#get filename of connectome file
        self.filename = tkinter.filedialog.askopenfilename(title='select connectome') 
        
    def select_list(self):#get filename of neurons list file
        self.neural_list_filename = tkinter.filedialog.askopenfilename(title='select neurons list') 

    def select_output(self): #get location of output
        self.filename_output = tkinter.filedialog.askdirectory(title='select output')

    def data_process(self): #get connectome, tau-list, and inverted connectome matrix
        print(self.filename)
        print(self.neural_list_filename)
        self.invConnectome, self.tau_list, self.neuronCount = process.process(self.filename,self.neural_list_filename, int(self.E1.get()),int(self.E2.get()),float(self.E3.get()),int(self.E4.get()))
        print('Inverted Connectome')
        plt.spy(self.invConnectome)
        plt.show(block=False)

    def run_sim(self): #run simulation
        self.run_button['state'] = tk.DISABLED
        self.y = run.run(self.invConnectome, self.tau_list, int(self.spkt_E.get())) #call run
        print('Write to file')
        print(self.filename_output+'/voltage.csv')
        with open(self.filename_output+'/voltage.csv','w',newline='') as f:
            writer = csv.writer(f)
            for i in self.y:
                writer.writerow(i)
        print('Done')
        print(self.filename_output)
        self.run_button['state'] = tk.NORMAL
        tmp = np.array(self.y)
        tmp_plot = (1*(tmp>0)).tolist()
        plt.imshow(tmp_plot, cmap='Greys',  interpolation='nearest')
        plt.show(block=False)

    def plot(self): #generate raster plot with existing voltage file
        self.filename = tkinter.filedialog.askopenfilename(title='select voltage')
        plot_raster.plot_raster(self.filename,self.filename_output)

    def help(self): #help information
        help_info = """        Parameters restrictions:
        Ncluster <= # of Neurons
        NpC = # of Neurons/Ncluster
        Connectivity <= NpC
        Topology: 1D/2D

        Steps:
        1. Select connectivity-list
        2. Select neuron-list
        3. Set output spiking voltage file path
        4. Process: construct connectome, tau-list, and then invert connectome
        5. Set spiking time range
        6. Click run to simulate and display raster plot

        Note: 
        1. Click Raster Plot to select output spiking voltage file and show raster
        2. To generate different testing cases, run dataGenerator.py 
        """
        mb.showinfo("Help", help_info)
    
window = tk.Tk()
Simulator(window)
window.mainloop()
 
