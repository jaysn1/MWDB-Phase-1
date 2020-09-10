# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:46:53 2020

@author: Jaysn
"""

import pandas as pd


def wordify(QUANTIZED_PATH, file_no, window_length, stride):
    file_name = '{0}/{1}.csv'.format(QUANTIZED_PATH, file_no)
    data = pd.read_csv(file_name, header=None)
    word_file = []
    for sensor_id in range(len(data)):
        t = 0
        sensor_vector = []
        while (t + stride) < len(data.iloc[sensor_id,:]):
            word = []
            idx = [int(file_no), sensor_id, t]
            win_vector = list(data.iloc[sensor_id, t : (t+window_length)])
            
            word.append(idx)
            word.append(win_vector)
            sensor_vector.append(word)
            t += stride
        word_file.append(sensor_vector)
    return word_file

def save_word_file(WORD_FILE_PATH, file_no, word_file):
    file_name = '{0}/{1}.wrd'.format(WORD_FILE_PATH, file_no)
    with open(file_name,'w+') as file:
        file.write(str(word_file))
            
            