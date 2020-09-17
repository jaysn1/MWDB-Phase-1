# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:39:02 2020

@author: Jaysn
"""
import pandas as pd
from Normalizer import Normalizer
from Quantizer import Quantizer
from Vectorizer import Vectorizer

from Vectorizer import TF_Calculator

def do_task_4(query_file, resolution, file_no, window_length, stride):
    query_data = pd.read_csv(query_file, header=None)
    normalized_query = Normalizer.normalizer(query_data)
    normalized_query = normalized_query.transpose()
    
    range_starts = Quantizer.calculate_lengths(resolution)
    quantized_query = Quantizer.quantize(normalized_query, range_starts)
    
    wordified_query = Vectorizer.wordify(quantized_query, file_no, window_length, stride)
    
    
    TFs = TF_Calculator.get_TF_of_words(wordified_query)
    
    
    # return TFs

# TFs= do_task_4('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z/1.csv', 3, 61, 3, 2)