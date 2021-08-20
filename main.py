# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:23:57 2021

@author: laukkara

Jos ei pysty antamaan kunnon arviota siitä, että millaiset olosuhteet
rakenteeseen muodostuu, niin pystyykö silloin rakennetta ylipäätään
kohtuullisella tarkkuudella edes suunnittelemaan?


"""
print('Begin!')


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import trh



case_name = 'US_1'

fname_input = os.path.join(r'C:\Local\laukkara\Data\github\trh-1',
                           'database_read_only', case_name, 'data.txt')

output_folder = os.path.join(r'C:\Local\laukkara\Data\OneDrive - TUNI.fi' \
                             r'\Rakennusfysiikka 2021\T RH mittaukset',
                             'output', case_name)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)



data = pd.read_csv(fname_input,
                   header=[0,1],
                   index_col=0,
                   parse_dates=[0])

T_i = data.loc[:, ('sisailma', 'T')]
RH_i = data.loc[:, ('sisailma', 'RH')]

T_e = data.loc[:, ('fmi', 'T')]
RH_e = data.loc[:, ('fmi', 'RH')]

# measurement_point_name = 'nurkka_oik_alh_MWup'
measurement_point_name = 'lammoneriste_MWup'

measurement_point_MG_classes = {'MG_speed': 'mr',
                                'MG_max': 'mr',
                                'C_mat': 0.1}

T_x = data.loc[:, (measurement_point_name, 'T')]
RH_x = data.loc[:, (measurement_point_name, 'RH')]


obj = trh.Trh(T_i, RH_i,
                T_e, RH_e,
                T_x, RH_x,
                output_folder,
                measurement_point_name,
                measurement_point_MG_classes)



print('End!')