# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:08:03 2020

@author: Jaysn
"""
import math
from tqdm import tqdm

    
def calculate_IDF(documents_gesture_wise_flatten_dict, total_files):  
    word_set = set()
    for file_no, document in documents_gesture_wise_flatten_dict.items():
        word_set.update(set(document))
        
    # return word_sets
    N = total_files
    IDFs_dict = {}
    
    for word in word_set:
        m = 0
        for document in documents_gesture_wise_flatten_dict.values():
            if word in document:
                m += 1
        if m != 0:
            idf = math.log(N/m)
            IDFs_dict[word] = idf
    return IDFs_dict

def calculate_IDF2(documents_gesture_wise_dict, total_files):
    word_sets = {}
    for file_no, documents in documents_gesture_wise_dict.items():
        gesture_word_set = set()
        for document in documents:
            gesture_word_set.update(document)
        word_sets[file_no] = gesture_word_set
    # return word_sets
    N = len(documents)
    IDFs_dict_2 = {}
    
    for file_no, words in tqdm(word_sets.items()):
        gesture_IDFs = {}
        for word in words:
            m = 0
            for document in documents_gesture_wise_dict[file_no]:
                if word in document:
                    m += 1
            
            if m != 0:
                idf = math.log(N/m)
                gesture_IDFs[word] = idf
        IDFs_dict_2[file_no] = gesture_IDFs
    return IDFs_dict_2
    