# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:23:57 2021

@author: Anssi Laukkarinen 2021


"""
print('Begin!')


import os
import pandas as pd
import trh


#############################
# Update input data here

structure_folder = os.path.join('.',
                                'database_read_only',
                                'omakotitalo_1',
                                'US_1')

#measurement_point_name = 'rajapinta_lammoneriste_tuulensuoja'
measurement_point_name = 'kulma_runkotolppa_tuulensuoja_oikealla_ylhaalla'
#measurement_point_name = 'nurkka_alaohjauspuu_runkotolppa_tuulensuoja_alhaalla_oikealla'
#measurement_point_name = 'nurkka_alaohjauspuu_runkotolppa_tuulensuoja_alhaalla_vasemmalla'
#measurement_point_name = 'rajapinta_lammoneriste_tuulensuoja'
#measurement_point_name = 'tuuletusvali'

measurement_point_MG_classes = {'MG_speed': 'vs',
                                'MG_max': 'vs',
                                'C_mat': 0.5}

###################################

# Read in data
print('Reading in data...')

csv_files = [f for f in os.listdir(structure_folder) if f.endswith('.csv')]

data = {}

for csv_file in csv_files:
    fname = os.path.join(structure_folder, csv_file)
    data[csv_file[:-4]] = pd.read_csv(fname,
                                      index_col=0,
                                      parse_dates=True)

for key in data:
    print(key)
print('\n')



print('Creating output folder...')
output_folder = structure_folder.replace('database_read_only', 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
print('\n')



print('Running TRH-1...')
T_i = data['sisailma'].loc[:, 'T']
RH_i = data['sisailma'].loc[:, 'RH']

T_e = data['fmi'].loc[:, 'T']
RH_e = data['fmi'].loc[:, 'RH']

T_x = data[measurement_point_name].loc[:, 'T']
RH_x = data[measurement_point_name].loc[:, 'RH']


obj = trh.TRH(T_i, RH_i,
              T_e, RH_e,
              T_x, RH_x,
              output_folder,
              measurement_point_name,
              measurement_point_MG_classes)



print('End!')