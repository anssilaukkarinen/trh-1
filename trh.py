# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:28:36 2021

@author: laukkara
"""

import os
import numpy as np
import matplotlib.pyplot as plt



class Trh():
    
    """
    Python class TRH for holding data and calculating indicators
    The input data is given as pandas dataframe with datetime index
    """
    
    def __init__(self,
                 T_i, RH_i,
                 T_e, RH_e,
                 T_x, RH_x,
                 output_folder,
                 measurement_point_name):
        
        # Initialisations
        self.T_i = T_i
        self.RH_i = RH_i
        
        self.T_e = T_e
        self.RH_e = RH_e
        
        self.T_x = T_x
        self.RH_x = RH_x
        
        self.output_folder = output_folder
        self.measurement_point_name = measurement_point_name
        
        self.fname_logfile = os.path.join(self.output_folder, 'log.txt')
        
        
        
        # Calculations and plotting
        self.make_basic_plots()
        
        # id 1: RH < RH_max
        self.calc_RH_x_max_const()
        
        # Add other indicator variables here...
        # Lue artikkelista, että mitä tähän voisi sopia
        
        
    
    
    def make_basic_plots(self):
        
        # Plot, sisäilma
        
        
        # Plot, fmi
        
        
        
        # Plot, x
        fig = plt.figure()
        ax = fig.gca()
        self.T_x.plot(grid='on',
                       ax=ax)
        fname = os.path.join(self.output_folder,
                             self.measurement_point_name + '_T_x.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        fig = plt.figure()
        ax = fig.gca()
        self.RH_x.plot(grid='on',
                       ax=ax)
        fname = os.path.join(self.output_folder,
                             self.measurement_point_name + '_RH_x.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        
        
    def calc_RH_x_max_const(self):
        
        # Calculate
        self.RH_x_max_const = np.max(self.RH_x)
        
        # Print to file
        with open(self.fname_logfile, 'w') as f:
            print('RH_x_max_const: ' + str(self.RH_x_max_const.round(2)),
                  file=f)
        

        
        
        
        
        
        
        
        

    
    
    
    
        
        
        
        
        
    
    