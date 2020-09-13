# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:56:44 2020

@author: Jaysn
"""
import collections
from tqdm import tqdm

def term_frequency(words):
    K = len(words)
    counts = {}
    for word in words:
        # if not counts[word]:
        counts[word] = words.count(word)
    for k, count in counts.items():
        counts[k] = count/K
    return counts


def calculate_TF(WORD_FILE_PATH, total_files):
    TFs_dict = {}
    
    for file_no in tqdm(range(1, total_files+1)):
        file_name = '{0}/{1}.wrd'.format(WORD_FILE_PATH, file_no)
        with open(file_name, 'r') as word_file:
            gesture_words = word_file.read()
        gesture_words = eval(gesture_words)
        gesture_trem_frequency = []
        for sensor_id in range(len(gesture_words)):
            sensor_gesture_words = list(map(lambda x: x[1], gesture_words[sensor_id]))
            termFrequencies = term_frequency(sensor_gesture_words)
            gesture_trem_frequency.append(termFrequencies)
        TFs_dict[file_no] = gesture_trem_frequency
    return TFs_dict