# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:28:36 2021

@author: laukkara
"""

import os
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



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
        with open(self.fname_logfile, mode='w', encoding='utf-8') as f:
            f.write('TRH-1 log file\n')
            time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write('Starting at ' + time_str + '\n\n')
        
        
        
        # Calculations and plotting
        self.make_basic_plots()
        
        # id 1: Comparison to maximum value
        self.calc_RH_x_ecdf()
        
        # id 2: Comparison to critical values
        self.calc_RH_x_crit()
        
        # Add other indicator variables here...
        # Lue artikkelista, että mitä tähän voisi sopia
        
        
    
    
    def make_basic_plots(self):
        
        
        self.xaxis_fmt = mdates.DateFormatter('%Y-%m-%d')
        
        # Plot, i
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.T_i.index, self.T_i.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'T_i.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.RH_i.index, self.RH_i.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_i.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        # Plot, e
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.T_e.index, self.T_e.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'T_e.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.RH_e.index, self.RH_e.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_e.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        

        
        # Plot, x
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.T_x.index, self.T_x.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'T_x_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.RH_x.index, self.RH_x.values)
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        

        
        
    
    def calc_RH_x_ecdf(self):
        # Use RH only by comparing the RH data to a limit value
        # ecdf = Empirical cumulative distribution function
        # 0, 50 and 100 (%) are the minimum, median and maximum
        
        # To file
        p = [100, 99.9, 99.5, 99, 95, 90, 75, 50,
             25, 10, 5, 1, 0.5, 0.1, 0]
        
        self.RH_x_ecdf = np.zeros( (len(p), 2) )
        
        for idx, p_val in enumerate(p):
            self.RH_x_ecdf[idx, 0] = p_val
            self.RH_x_ecdf[idx, 1] = np.percentile(self.RH_x, p_val)
        
        with open(self.fname_logfile, 'a') as f:
            f.write('RH_x empirical cumulative distribution function:\n')
            f.write('<Percentile 0-100> <RH 0-100>\n')
            np.savetxt(f, self.RH_x_ecdf, fmt='%.02f')
            f.write('\n\n')
        
        
        # Plot, cdf
        x = np.sort(self.RH_x)
        y = np.linspace(start=0.0, stop=1.0, num=len(x))
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(x, y)
        ax.set_xlabel('RH_x, %')
        ax.set_ylabel('ecdf, 0-1')
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_ecdf_' + self.measurement_point_name  + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        # Plot, icdf
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(y, x)
        ax.set_ylabel('RH_x, %')
        ax.set_xlabel('ecdf, 0-1')
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_icdf_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
    
    @staticmethod
    def calc_RH_crit(T):
        n = len(T)
        RH_crit = np.zeros(n)
        
        for idx in range(n):
            
            if T[idx] <= 1.0:
                RH_crit[idx] = 0.83*T[idx] + 97.0
            else:
                RH_crit[idx] = \
                    np.maximum(-0.00267*T[idx]**3 + 0.16*T[idx]**2 - 3.13*T[idx] + 100.0,
                               80.0)
        return(RH_crit)

    
    
    
            
    def calc_RH_x_crit(self):
        # Use both RH and T to create a two-dimensional limit curve
        
        self.RH_x_crit = self.calc_RH_crit(self.T_x)
                
        
        # plot
        T_min = self.T_x.min()
        T_max = self.T_x.max()
        T_vals = np.linspace(start=T_min, stop=T_max)
        RH_vals = self.calc_RH_crit(T_vals)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(self.T_x, self.RH_x, '.', markersize=0.6)
        ax.plot(T_vals, RH_vals)
        ax.set_xlabel('T, C')
        ax.set_ylabel('RH, %')
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_crit_scatter_' \
                                 + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        # Proportion of points over the curve
        n_pos = np.sum(self.RH_x > self.RH_x_crit)
        n_tot = len(self.RH_x)
        
        s = 'Datapisteiden määrä rajakäyrän yläpuolella: {} kpl / {} kpl = {} %' \
            .format(n_pos, n_tot, np.round(100*n_pos/n_tot, 2))
        print(s)
        
        with open(self.fname_logfile, 'a') as f:
            f.write(s + '\n')
            f.write('\n\n')
        
        
        # Total time over the curve
        idxs = self.RH_x > self.RH_x_crit
        
        dt_total = self.RH_x.index.to_series().diff().sum()
        dt_over_curve = self.RH_x.index.to_series().diff().loc[idxs].sum()
        
        n_total_days = dt_total / pd.Timedelta(days=1)
        n_over_curve_days = dt_over_curve / pd.Timedelta(days=1)
        
        
        s = 'Aika rajakäyrän yläpuolella: {} vrk / {} vrk = {} %' \
            .format(n_over_curve_days, n_total_days,
                    np.round(100*n_over_curve_days/n_total_days, 2))
        print(s)
        with open(self.fname_logfile, 'a') as f:
            f.write(s + '\n')
            f.write('\n\n')
    
        
        
        
            
        
        
        

        
        
        
        
        
        
        
        

    
    
    
    
        
        
        
        
        
    
    