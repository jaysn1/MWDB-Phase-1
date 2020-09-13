# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:35:29 2020

@author: Jaysn
"""
import math
from scipy.integrate import quad
import pandas as pd
from tqdm import tqdm

MEAN = 0
SD = 0.25
PI = math.pi 

def guassian(x):
    a = 1/ (SD * math.sqrt(2*PI))
    e = (-1 * math.pow((x - MEAN),2)) / (2 * math.pow(SD, 2))
    return a * math.exp(e)

def calculate_lengths(resolution):
    lengths = []
    range_starts = [-1]
    
    # Calculate guassian band lengths
    for i in range(1, (2 * resolution) + 1):
        lower_limit = (i - resolution - 1) / resolution
        upper_limit = (i - resolution) / resolution
        numerator = quad(guassian, lower_limit, upper_limit)[0]
        denominator = quad(guassian, -1, 1)[0]
        length = (2 * numerator) / denominator
        lengths.append(length)
        range_starts.append(range_starts[-1] + length)
    # print(range_starts)
    # print(lengths)
    range_starts[0] = -1.1
    return range_starts

def quantize(data_file, range_starts):
    quantized_file = []
    
    # Quantize individual file
    for row in range(len(data_file)):
        quantized_row = []
        for col in range(len(data_file.iloc[row,:])):
            i = 0
            while i < len(range_starts) and float(data_file.iloc[row, col]) > range_starts[i]:
                i += 1
            quantized_row.append(i)
        quantized_file.append(quantized_row)
    quantized_file = pd.DataFrame(quantized_file)
    return quantized_file
    # print(quantized_file))
    # print(pd.DataFrame(quantized_file))
    
        

def save_quantized_files(NORMALIZED_PATH, QUANTIZED_PATH, total_files, range_starts):
    
    # Call and save quantize function for all files
    print("\nQuantizing all files...")
    for i in tqdm(range(1, total_files + 1)):
        file_to_get = '{0}/{1}.csv'.format(NORMALIZED_PATH, i)
        df = pd.read_csv(file_to_get, header=None)
        quantized_file = quantize(df, range_starts)
        
        file_name = '{0}/{1}.csv'.format(QUANTIZED_PATH, i)
        quantized_file.to_csv(file_name, index=False, header=False)
        

        
        
        
        
        
        
        
        