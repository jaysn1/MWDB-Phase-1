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
        TFIDFs_dict[file_no] = []
        for i, tfs in enumerate(gesture_tfs):
            gesture_sensor_tfidf = {}
            idfs = IDFs_dict[i+1]
            max_freq = max(tfs.values())
            for word, tf in tfs.items():
                idf = idfs[word]
                word_tfidf = tfidf(tf, idf, max_freq)
                gesture_sensor_tfidf[word] = word_tfidf
            TFIDFs_dict[file_no].append(gesture_sensor_tfidf)
    return TFIDFs_dict
            
def calculate_TFIDF_2(term_frequencies_dict, IDFs_dict_2):
    TFIDFs_dict_2 = {}
    for file_no, gesture_tfs in tqdm(term_frequencies_dict.items()):
        TFIDFs_dict_2[file_no] = []
        for i, tfs in enumerate(gesture_tfs):
            gesture_sensor_tfidf_2 = {}
            idfs = IDFs_dict_2[file_no]
            max_freq = max(tfs.values())
            for word, tf in tfs.items():
                idf = idfs[word]
                word_tfidf_2 = tfidf(tf, idf, max_freq)
                gesture_sensor_tfidf_2[word] = word_tfidf_2
            TFIDFs_dict_2[file_no].append(gesture_sensor_tfidf_2)
    return TFIDFs_dict_2