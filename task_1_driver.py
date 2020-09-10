# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:22:36 2020

@author: Jaysn
"""
from Normalizer import Normalizer
from Quantizer import Quantizer
from Vectorizer import Vectorizer
from tqdm import tqdm

def get_normalized_files(PATH, NORMALIZED_PATH, total_files):
    data, file_sizes = Normalizer.get_files(PATH, total_files)
    normalized_data = Normalizer.normalizer(data).transpose()
    Normalizer.split_files(normalized_data, NORMALIZED_PATH, file_sizes)
    return normalized_data

def get_quantized_files(NORMALIZED_PATH, QUANTIZED_PATH, total_files, resolution):
    range_starts = Quantizer.calculate_lengths(resolution)
    Quantizer.save_quantized_files(NORMALIZED_PATH, QUANTIZED_PATH, total_files, range_starts)

def get_word_files(QUANTIZED_PATH, WORD_FILE_PATH, total_files, window_length, stride):
    for file_no in tqdm(range(1, total_files+1)):
        word_file = Vectorizer.wordify(QUANTIZED_PATH, file_no, window_length, stride)
        Vectorizer.save_word_file(WORD_FILE_PATH, file_no, word_file)
    
    
def do_task_1(PATH, NORMALIZED_PATH, QUANTIZED_PATH, WORD_FILE_PATH, total_files, resolution, window_length, stride):
    # data = get_normalized_files(PATH, NORMALIZED_PATH, total_files)
    Normalizer.normalize_file_wise(PATH, NORMALIZED_PATH, total_files)
    get_quantized_files(NORMALIZED_PATH, QUANTIZED_PATH, total_files, resolution)
    get_word_files(QUANTIZED_PATH, WORD_FILE_PATH, total_files, window_length, stride)
   
    # return data
# data = do_task_1('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z', 
#                  'C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/normalized_Z', 
#                  'C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/quantized_Z', 60, 3, 3, 2)