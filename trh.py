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

import fmgm



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
                 measurement_point_name,
                 measurement_point_MG_classes):
        
        # Initialisations
        self.T_i = T_i
        self.RH_i = RH_i
        
        self.T_e = T_e
        self.RH_e = RH_e
        
        self.T_x = T_x
        self.RH_x = RH_x
        
        self.output_folder = output_folder
        self.measurement_point_name = measurement_point_name
        self.measurement_point_MG_classes = measurement_point_MG_classes
        
        self.fname_logfile = os.path.join(self.output_folder,
                                          'log_' + self.measurement_point_name + '.txt')
        with open(self.fname_logfile, mode='w', encoding='utf-8') as f:
            f.write('TRH-1 log file\n')
            time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write('Starting at: ' + time_str + '\n\n')
        
        
        
        # Calculations and plotting
        self.make_basic_plots()
        
        # id 1: Comparison to maximum value
        self.calc_RH_x_ecdf()
        
        # id 2 and 3: Comparison to critical values
        self.calc_RH_x_crit()
        
        # id 4: M_max < 1
        self.calc_M_max()
        
        # id 4 and 5: VI and TI
        self.calc_VI_TI()
        
        
        with open(self.fname_logfile, mode='a') as f:
            time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write('Ending at: ' + time_str + '\n\n')
        
        
    
    
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
        
        print('np.percentile(RH_x, 99): {:0.1f}'.format(self.RH_x.values[0]))
        
        with open(self.fname_logfile, 'a') as f:
            f.write('RH_x empirical cumulative distribution function:\n')
            f.write('<Percentile 0-100> <RH 0-100>\n')
            np.savetxt(f, self.RH_x_ecdf, fmt='%.02f')
            f.write('\n')
        
        
        # Plot, cdf
        x = np.sort(self.RH_x)
        y = np.linspace(start=0.0, stop=1.0, num=len(x))
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(x, y)
        ax.set_xlabel('RHx, %')
        ax.set_ylabel('ecdf, 0-1')
        ax.set_xlim((-2, 102))
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_ecdf_' + self.measurement_point_name  + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        # Plot, icdf
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(y, x)
        ax.set_ylabel('RHx, %')
        ax.set_xlabel('ecdf, 0-1')
        ax.set_ylim((-2, 102))
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
        ax.set_ylim((-2, 102))
        ax.grid()
        fname = os.path.join(self.output_folder,
                             'RH_x_crit_scatter_' \
                                 + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        # Proportion of points over the curve
        n_pos = np.sum(self.RH_x > self.RH_x_crit)
        n_tot = len(self.RH_x)
        
        s = 'Datapisteiden määrä rajakäyrän yläpuolella: ' \
            '{} kpl / {} kpl = {:0.1f} %' \
            .format(n_pos, n_tot, 100*n_pos/n_tot)
        print(s)
        
        with open(self.fname_logfile, 'a') as f:
            f.write(s + '\n')
            f.write('\n')
        
        
        # Total time over the curve
        idxs = self.RH_x > self.RH_x_crit
        
        dt_total = self.RH_x.index.to_series().diff().sum()
        dt_over_curve = self.RH_x.index.to_series().diff().loc[idxs].sum()
        
        n_total_days = dt_total / pd.Timedelta(days=1)
        n_over_curve_days = dt_over_curve / pd.Timedelta(days=1)
        
        
        s = 'Aika rajakäyrän yläpuolella: ' \
            '{} vrk / {} vrk = {:0.1f} %' \
            .format(n_over_curve_days, n_total_days,
                    100*n_over_curve_days/n_total_days)
        print(s)
        with open(self.fname_logfile, 'a') as f:
            f.write(s + '\n')
            f.write('\n')
    
        
        
        
            
    def calc_M_max(self):
        # Calculate the maximum mould index from the measurement period
        # It would be good to have at least one year of data
        
        # Calculations
        T_x_M = self.T_x.resample('1h').interpolate('index')
        RH_x_M = self.RH_x.resample('1h').interpolate('index')
        
        t_idx = RH_x_M.index
        
        M_x_dummy = fmgm.MI(T_x_M,
                            RH_x_M,
                            self.measurement_point_MG_classes['MG_speed'],
                            self.measurement_point_MG_classes['MG_max'],
                            self.measurement_point_MG_classes['C_mat'])
        self.M_x = pd.DataFrame(data=M_x_dummy,
                                index=t_idx)
        
        self.M_x_max = np.max(self.M_x).values[0]
        
        
        # Plot
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(self.M_x)
        fname = os.path.join(self.output_folder,
                             'M_x_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        
        
        # print to terminal and file
        s = 'M_x_max: {}'.format( self.M_x_max )
        print(s)
        with open(self.fname_logfile, 'a') as f:
            f.write(s + '\n')
            f.write('\n')
        
        
    @staticmethod
    def vsat(T):
        # Calculate saturation vapour pressure
        pvsat = 611.2*np.exp((17.62*T)/(243.12+T))
        v_sat = pvsat/(461.5*(T+273.15))
        return(v_sat)
    
    
    def calc_VI_TI(self):
        # Calculate dv, dT, VI and TI
        # Tx = Ti - (Ry/Rtot)*(Ti-Te) -> (Ry/Rtot) = (Ti-Tx)/(Ti-Te)
        # Tx = Te + (Rx/Rtot)*(Ti-Te) -> (Rx/Rtot) = (Tx-Te)/(Ti-Te) = TI
        
        # Calculations
        dT_x_e = self.T_x - self.T_e
        dT_i_e = self.T_i - self.T_e
        self.TI = dT_x_e.rolling(12*6).mean() / dT_i_e.rolling(12*6).mean()
        
        
        self.v_i = 1000.0 * self.vsat(self.T_i) * (self.RH_i / 100.0)
        self.v_e = 1000.0 * self.vsat(self.T_e) * (self.RH_e / 100.0)
        self.v_x = 1000.0 * self.vsat(self.T_x) * (self.RH_x / 100.0)
        
        dv_x_e = self.v_x - self.v_e
        dv_i_e = self.v_i - self.v_e
        self.VI = dv_x_e.rolling(12*6).mean() / dv_i_e.rolling(12*6).mean()
        
        
        # Plotting, dTdT and dvdv
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(dT_i_e, linewidth=0.7)
        ax.plot(dT_x_e, linewidth=0.7)
        ax.grid()
        ax.legend(['dT_i_e', 'dT_x_e'])
        ax.set_ylabel('dT, C')
        fname = os.path.join(self.output_folder,
                             'dT_dT_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(dv_i_e, linewidth=0.7)
        ax.plot(dv_x_e, linewidth=0.7)
        ax.grid()
        ax.legend(['dv_i_e', 'dv_x_e'])
        ax.set_ylabel('dv, g/m3')
        fname = os.path.join(self.output_folder,
                             'dv_dv_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        # plotting, TI and VI
        ylim_min_TI = np.percentile( self.TI[~self.TI.isna()] , 2)
        ylim_max_TI = np.percentile( self.TI[~self.TI.isna()] , 98)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.TI, '.', markersize=0.5)
        ax.grid()
        ax.set_ylabel('TI = (Tx-Te)/(Ti-Te), -')
        ax.set_ylim((ylim_min_TI, ylim_max_TI))
        fname = os.path.join(self.output_folder,
                             'TI_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        
        ylim_min_VI = np.percentile( self.VI[~self.VI.isna()] , 5)
        ylim_max_VI = np.percentile( self.VI[~self.VI.isna()] , 95)
        
        fig = plt.figure()
        ax = fig.gca()
        ax.xaxis.set_major_formatter(self.xaxis_fmt)
        fig.autofmt_xdate()
        ax.plot(self.VI, '.', markersize=0.5)
        ax.grid()
        ax.set_ylabel('VI = (vx-ve)/(vi-ve), -')
        ax.set_ylim((ylim_min_VI, ylim_max_VI))
        fname = os.path.join(self.output_folder,
                             'VI_' + self.measurement_point_name + '.png')
        fig.savefig(fname, dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        