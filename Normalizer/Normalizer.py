# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 03:15:40 2020

@author: Jaysn
"""
import pandas as pd


def get_files(PATH, total_files):
    
    data = pd.DataFrame()
    file_sizes = []
    
    # Collect all data in a single variable to normalize accross all files
    for file_no in range(1, total_files+1):
        file_name = '{0}/{1}.csv'.format(PATH, file_no)
        df = pd.read_csv(file_name, header=None)
        data = pd.concat([data, df], axis=1, ignore_index=True)
        file_sizes.append(len(df.columns))
    return data, file_sizes
    
def normalizer(data):
    normalized_data = []
    MINIMUM_VALUE = -1
    
    # Normalize data row-wise or sensor-wise
    for i in range(len(data)):
        row = data.iloc[i,:]
        norm_temp = [MINIMUM_VALUE + ((data.iloc[i,j] - min(row)) / (max(row) - min(row))) for j in range(len(row))]
        normalized_data.append(norm_temp)
    return normalized_data


def get_normalized_files(PATH, total_files):
    data, file_sizes = get_files(PATH, total_files)
    print(data)
    normalized_data = normalizer(data)
    print(normalized_data)
    return normalized_data

data = get_normalized_files('C:\Users\Jaysn\Anaconda3\envs\MWDB_Phase_1\src\Data\Z', 60)