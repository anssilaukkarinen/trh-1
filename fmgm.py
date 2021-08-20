# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:38:09 2021

Mould index according to the Finnish Mould Growth Model

Python implementation: Anssi Laukkarinen 2011-2016
"""



def MI(dataT,dataRH,MGspeedclass,MGmaxclass,Cmat):    
    """
    # Introduction
    This function uses the VTT-TUT model to calculate the mould index.

    The model is based on the mould growth model created in the Technical
    Reasearch Center of Finland (VTT) and updated in a recent project between
    VTT and Tampere University of Technology (TUT) during 2005-2009.

    More material, laboratory and field tests were performed and new mould
    sensitivity and decline classes were created to assess the mould growth on
    different materials.

    In the interface of two materials the mould growth speed is determined by
    the more sensitive material. The maximum value of mould index is determined
    by the material studied.

    Some materials can belong to two different sensitivity classes e.g.
    lightweight concrete. For this material the mould growth speed is
    determined by the 'sensitive' class and the maximum mould index value is
    determined by the 'resistant' sensitivity class.

    Time step is always one hour

    Temperature is is degrees Celsius and RH is in % (0...100)

    # Sensitivity and decline classes
    Sensitivity classes:
        Very sensitive: vs
        Sensitive: s
        Medium resistant: mr
        Resistant: r
    Mould decline/recession factors:
        Strong decline sd: Cmat = 0.5
        Remarkable decline rd: Cmat = 0.25
        Moderate(relatively low) decline md: Cmat = 0.1
        Low (almost no) decline ld: Cmat = 0.1

    Thin underlay: mr/0.1
    Glass wool: mr/0.1
    Wood fibreboard: s/0.25
    wood hardboard: s/0.25
    concrete: mr/0.25
    leca: mr/0.1
    sand: mr/0.1
    cellulose insulation: s/0.25

    Materials on different mould sensitivity classes:
    Very sensitive:
    pine sapwood
    Untreated wood, materials including nutrients
    sawn pine and spruce
    paper coated products 

    Sensitive:
    Planed wood
    paper coated products
    wood based boards
    lightweight concrete (mould growth speed)

    Medium resistant:
    cement based materials
    plastic based materials
    mineral fibers
	lightweight concrete (maximum mould growth index)

    Resistant:
    Glass products
    Metal products
    Materials with protective compound treatment
    


    About mould index decline:
    Strong decline:

    Remarkable decline:
    sawn spruce
    sawn pine
    lightweight concrete

    Moderate decline:
    planed spruce
    planed pine
    concrete
    paper coated PUR
    glass wool

    Low decline:
    lighweight expanded clay aggregate
    polyester fibre insulation
    EPS
    #####
    Frame final report:
    
    Very sensitive:
        rough sawn and dimensionalized pine and spruce
        planed pine
    
    Sensitive:
        planed spruce
        paper-based product and foils
        wood-based boards
        gypsum board
        lightweight concrete (speed)
    
    Medium resistant:
        mineral wool
        plastic-based materials
        lightweight concrete (max)
        lightweight aggregate concrete
        carbonized concrete
        cement-based products
        bricks
    
    Resistant:
        glass and metal
        alkaline concrete
        materials containing mould-protective compounds
    
    Cmat
        vs HHL1 - HTL2 0.5
        s HHL2 - HTL3 0.25
        mr HHL3 - HTL4 0.1
        r HHL4 - HTL4 0.1
    
    
    ########
    # Example 1, just to get started    
    import numpy as np
    import matplotlib.pyplot as plt
    % matplotlib inline

    tmax = 120*168
    t = np.arange(0, tmax/168+0.01, 1/168)
    T = 22 * np.ones(len(t))
    RH = 90 * np.ones(len(t))
    Mspeedclass = 's'
    Mmaxclass = 's'
    Cmat = 0.25

    Mvals = tutpy.MI(T, RH, Mspeedclass, Mmaxclass, Cmat)

    plt.plot(t, Mvals)
    plt.xlim([0, 120])
    plt.ylim([0, 6])
    plt.grid()
    """
    
    import numpy as np

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
