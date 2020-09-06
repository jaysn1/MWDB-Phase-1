# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 03:15:40 2020

@author: Jaysn
"""
import pandas as pd
from tqdm import tqdm


def get_files(PATH, total_files):
    
    data = pd.DataFrame()
    file_sizes = []
    
    # Collect all data in a single variable to normalize accross all files
    for file_no in tqdm(range(1, total_files+1)):
        file_name = '{0}/{1}.csv'.format(PATH, file_no)
        df = pd.read_csv(file_name, header=None)
        data = pd.concat([data, df], axis=1, ignore_index=True)
        file_sizes.append(len(df.columns))
    return data, file_sizes
    
def normalizer(data):
    normalized_data = pd.DataFrame()
    MINIMUM_VALUE = -1
    MAXIMUM_VALUE = 1
    
    # Normalize data row-wise or sensor-wise
    for i in range(len(data)):
        row = data.iloc[i,:]
        minimum = min(row)
        maximum = max(row)
        norm_temp = pd.DataFrame([MINIMUM_VALUE + ((MAXIMUM_VALUE - MINIMUM_VALUE) * (data.iloc[i,j] - minimum) / (maximum - minimum)) for j in range(len(row))])
        normalized_data = pd.concat([normalized_data, norm_temp], axis=1, ignore_index=True)
    return normalized_data

def split_files(normalized_data, NORMALIZED_PATH, file_sizes):
    file_start_index = 0
    
    # Create normalized csv files
    for key, file_size in enumerate(file_sizes):
        normalized_gesture_data = normalized_data.iloc[ :, file_start_index : file_start_index+file_size]
        file_start_index += file_size
        file_name = '{0}/{1}.csv'.format(NORMALIZED_PATH, key+1)
        normalized_gesture_data.to_csv(file_name, index=False, header=False)

