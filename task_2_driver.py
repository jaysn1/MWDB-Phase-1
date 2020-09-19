# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:11:48 2020

@author: Jaysn
"""
import numpy as np
from tqdm import tqdm
import time
from Vectorizer import DocumentGenerator
from Vectorizer import TF_Calculator
from Vectorizer import IDF_Calculator
from Vectorizer import TFIDF_Calculator
import config
import json


def save_vectors_file(documents_gesture_wise_dict, TFs_dict, TFIDFs_dict, TFIDFs_dict_2, VECTOR_FILE_PATH, total_files):
    vectors = {}
    for file_no in tqdm(range(1, total_files+1)):
        
        TFs = TFs_dict[file_no]
        TFIDFs = TFIDFs_dict[file_no]
        TFIDF_2s = TFIDFs_dict_2[file_no]
        
        gesture_vectors = []
        for sensor_id, sensor_words in enumerate(documents_gesture_wise_dict[file_no]):
            vector = []
            for word in sensor_words:
                word_vector = tuple([TFs[word], TFIDFs[word], TFIDF_2s[word[1:]]])
                vector.append(word_vector)
            gesture_vectors.append(vector)
        vectors[file_no] = gesture_vectors
        
    file_name = '{0}/vectors.txt'.format(VECTOR_FILE_PATH)
    with open(file_name, 'w+') as file:
        file.write(str(vectors))
        
        
def do_task_2(WORD_FILE_PATH, VECTOR_FILE_PATH, total_files):
    documents_gesture_wise_dict, documents_gesture_wise_flatten_dict, TFs_dict, IDFs_dict, IDFs_dict_2, TFIDFs_dict, TFIDFs_dict_2 ={}, {}, {}, {}, {}, {}, {}
    
    print("\nGetting document words dictionary (gesture wise)...")
    documents_gesture_wise_flatten_dict, documents_gesture_wise_flatten_for_tf2_dict = DocumentGenerator.get_documents_1(WORD_FILE_PATH, total_files)
    documents_gesture_wise_dict, documents_gesture_wise_for_IDF2_dict = DocumentGenerator.get_documents_2(WORD_FILE_PATH, total_files)
        
    print("\nGetting Term Frequencies...")
    TFs_dict, TFs_2_dict = TF_Calculator.calculate_TF(documents_gesture_wise_flatten_dict, documents_gesture_wise_flatten_for_tf2_dict)
    
    print("\nGetting IDFs...")
    IDFs_dict = IDF_Calculator.calculate_IDF(documents_gesture_wise_flatten_dict, total_files)
    
    print("\nGetting IDFs 2...")
    IDFs_dict_2 = IDF_Calculator.calculate_IDF2(documents_gesture_wise_for_IDF2_dict, total_files)
    
    print("\nCalculating TF-IDFs...")
    TFIDFs_dict = TFIDF_Calculator.calculate_TFIDF(TFs_dict, IDFs_dict)
    
    print("\nCalculating TF-IDF2s...")
    TFIDFs_dict_2 = TFIDF_Calculator.calculate_TFIDF_2(TFs_2_dict, IDFs_dict_2)
    
    print("\nSaving Vectors...")
    save_vectors_file(documents_gesture_wise_dict, TFs_dict, TFIDFs_dict, TFIDFs_dict_2, VECTOR_FILE_PATH, total_files)
    
    with open('TF.txt', 'w') as f:
        f.write(str(TFs_dict))
    with open('IDF.txt', 'w') as f:
        f.write(str(IDFs_dict))
    with open('TFIDF.txt', 'w') as f:
        f.write(str(TFIDFs_dict))
    with open('TFIDF_2.txt', 'w') as f:
        f.write(str(TFIDFs_dict_2))
    
    # return documents_gesture_wise_dict, documents_gesture_wise_for_IDF2_dict, documents_gesture_wise_flatten_dict, documents_gesture_wise_flatten_for_tf2_dict, TFs_dict, TFs_2_dict, IDFs_dict, IDFs_dict_2, TFIDFs_dict, TFIDFs_dict_2 
    
# documents_gesture_wise_dict, documents_gesture_wise_for_IDF2_dict, documents_gesture_wise_flatten_dict, documents_gesture_wise_flatten_for_tf2_dict, TFs_dict, TFs_2_dict, IDFs_dict, IDFs_dict_2, TFIDFs_dict, TFIDFs_dict_2 = do_task_2('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Word_Files', 'C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z', 66)