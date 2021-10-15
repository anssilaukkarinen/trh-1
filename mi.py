# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:38:09 2021

Mould index according to the Finnish Mould Growth Model

Python implementation: Anssi Laukkarinen 2011-2016
"""

import numpy as np


def MI(dataT, dataRH, MGspeedclass, MGmaxclass, Cmat):

    # Array for mold index values is created to avoid resizing
    M = np.zeros(dataT.size)

    # Time from the beginning of the mould decline
    TFR = 0


    # Determining the factors for k2
    # These are constant throughout the calculation
    # They are used to calculate the Mmax
    if MGmaxclass == 'vs':
        A = 1
        B = 7
        C = 2
    elif MGmaxclass == 's':
        A = 0.3
        B = 6
        C = 1
    elif MGmaxclass == 'mr':
        A = 0
        B = 5
        C = 1.5
    elif MGmaxclass == 'r':
        A = 0
        B = 3
        C = 1

    # RHmin is determined, it is also in the calculation of Mmax
    if MGspeedclass == 'vs':
        RHmin = 80
    elif MGspeedclass == 's':
        RHmin = 80
    elif MGspeedclass == 'mr':
        RHmin = 85
    elif MGspeedclass == 'r':
        RHmin = 85

    # Next the actual calculation
    for k in range(dataT.size - 1):

        # First the limit value for RH
        if dataT[k] < 0.0:
            RHcrit=100
        else:
            RHcrit = np.max([-0.00267*dataT[k]**3 + 0.16*dataT[k]**2 \
                -3.13*dataT[k]+100, RHmin])

        # Then mould growth/decline speed calculation
        if dataT[k]>0.0 and dataT[k]<50.0 and dataRH[k]>=RHcrit:
            # Mould grows

            dummy1 = (RHcrit-dataRH[k])/(RHcrit-100.0)
            Mmax = np.max([A + B*dummy1 - C*dummy1**2, 0.0])

            if M[k] < 1.0:
                if MGspeedclass == 'vs':
                    k1 = 1
                elif MGspeedclass == 's':
                    k1 = 0.578
                elif MGspeedclass == 'mr':
                    k1 = 0.072
                else:
                    k1 = 0.033
                    
            else:
                if MGspeedclass == 'vs':
                    k1 = 2
                elif MGspeedclass == 's':
                    k1 = 0.386
                elif MGspeedclass == 'mr':
                    k1 = 0.097
                else:
                    k1 = 0.014

            # Time from the beginning of the recession
            TFR = 0
            k2 = np.max([1.0-np.exp(2.3*(M[k]-Mmax)), 0.0])
            
            # log() calculates natural logarithm
            # Two parameters from the old model are removed (+0.14*W-0.33*SQ)
            dummy2 = -0.68*np.log(dataT[k]) - 13.9*np.log(dataRH[k]) + 66.02
            dMdt = (1.0/(7*np.exp(dummy2))) * k1 * k2 * (1.0/24.0)

        else:
            # Mould doesn't grow
                                                     
            # Time from the beginning of recession
            TFR = TFR + 1
            
            if TFR <= 6:
                dMdt0 = -0.032*(1/24)
            elif TFR >6 and TFR <=24:
                dMdt0 = 0
            else:
                dMdt0 = -0.016*(1/24)

            # The dMdt is sometimes written as (dM0/dt)mat
            # Time step is one hour
            dMdt = Cmat * dMdt0*1

        # Calculation of the new mould index value
        # New mould index value, one hour time step
        M[k+1] = np.max([M[k]+dMdt*1, 0])
    return(M)
