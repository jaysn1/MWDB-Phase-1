# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:22:36 2020

@author: Jaysn
"""
from Normalizer import Normalizer
from Quantizer import Quantizer

def get_normalized_files(PATH, NORMALIZED_PATH, total_files):
    data, file_sizes = Normalizer.get_files(PATH, total_files)
    normalized_data = Normalizer.normalizer(data).transpose()
    Normalizer.split_files(normalized_data, NORMALIZED_PATH, file_sizes)

def get_quantized_files(resolution):
    lengths = Quantizer.calculate_lengths(resolution)
    print(lengths)

def do_task_1(PATH, NORMALIZED_PATH, total_files, resolution):
    get_normalized_files(PATH, NORMALIZED_PATH, total_files)
    get_quantized_files((resolution))
    
# do_task_1('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z', 'C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/normalized_Z', 60, 3)