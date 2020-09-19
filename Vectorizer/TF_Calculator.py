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
    word_set = set(words)
    for word in word_set:
        # if not counts[word]:
        counts[word] = words.count(word)
    for k, count in counts.items():
        counts[k] = count/K
    return counts


def calculate_TF(documents_gesture_wise_flatten_dict, documents_gesture_wise_flatten_for_tf2_dict):
    TFs_dict = {}
    TFs_2_dict = {}
    
    for file_no, gesture_words in tqdm(documents_gesture_wise_flatten_dict.items()):
        gesture_term_frequency = term_frequency(gesture_words)
        TFs_dict[file_no] = gesture_term_frequency
    for file_no, gesture_words in tqdm(documents_gesture_wise_flatten_for_tf2_dict.items()):
        gesture_term_frequency = term_frequency(gesture_words)
        TFs_2_dict[file_no] = gesture_term_frequency
        
    return TFs_dict, TFs_2_dict