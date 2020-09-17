# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:08:48 2020

@author: Jaysn
"""
from tqdm import tqdm

def tfidf(tf, idf, max_freq):
    b = 0.5 + (0.5 * tf)/max_freq
    return b * idf

def calculate_TFIDF(term_frequencies_dict, IDFs_dict):
    
    TFIDFs_dict = {}        
    for file_no, gesture_tfs in tqdm(term_frequencies_dict.items()):
        TFIDFs_dict[file_no] = {}
        max_freq = max(gesture_tfs.values())
        
        for word, tf in gesture_tfs.items():
            idf = IDFs_dict[word]
            
            word_tfidf = tfidf(tf, idf, max_freq)
            TFIDFs_dict[file_no][word] = word_tfidf
            
    return TFIDFs_dict
            
def calculate_TFIDF_2(term_frequencies_dict, IDFs_dict_2):
    TFIDFs_dict_2 = {}        
    for file_no, gesture_tfs in tqdm(term_frequencies_dict.items()):
        TFIDFs_dict_2[file_no] = {}
        max_freq = max(gesture_tfs.values())
        
        for word, tf in gesture_tfs.items():
            idf = IDFs_dict_2[file_no][word]
            word_tfidf_2 = tfidf(tf, idf, max_freq)
            TFIDFs_dict_2[file_no][word] = word_tfidf_2
    return TFIDFs_dict_2