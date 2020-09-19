# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:39:02 2020

@author: Jaysn
"""
import pandas as pd
from Normalizer import Normalizer
from Quantizer import Quantizer
from Vectorizer import Vectorizer
import math
import time
from Vectorizer import TF_Calculator
from Vectorizer import TFIDF_Calculator

def task_1(query_file, resolution, file_no, window_length, stride):
    query_data = pd.read_csv(query_file, header=None)
    normalized_query = Normalizer.normalizer(query_data)
    normalized_query = normalized_query.transpose()
    
    range_starts = Quantizer.calculate_lengths(resolution)
    quantized_query = Quantizer.quantize(normalized_query, range_starts)
    
    wordified_query = Vectorizer.wordify(quantized_query, file_no, window_length, stride)
    return wordified_query

def task_2(wordified_query):
    
    # Create documents
    document_query = []
    flattened_document_query = []
    for sensor_id, sensor_words in enumerate(wordified_query):
        words = list(map(lambda x : tuple([sensor_id+1] + x[1]), sensor_words))
        flattened_document_query.extend(words)
        document_query.append(words)
    
    # Get TFs
    TFs_dict_query = TF_Calculator.term_frequency(flattened_document_query)
    
    # Get IDFs
    with open('IDF.txt', 'r') as f:
        IDFs_dict = eval(f.read())
    IDFs_dict_query = {}
    word_sets = set(flattened_document_query)
    for word in word_sets:
        IDFs_dict_query[word] = IDFs_dict[word]
    
    
    # Get IDF2s
    IDFs_dict_2_query = {}
    N = len(wordified_query)
    for word in word_sets:
        m = 0
        for document in document_query:
            if word in document:
                m += 1
        
        if m != 0:
            idf = math.log(N/m)
            IDFs_dict_2_query[word] = idf
    
    # Get TFIDFs and TFIDF2s
    TFIDFs_dict_query = {}
    TFIDFs_dict_2_query = {}
    max_freq = max(TFs_dict_query.values())
    for word, tf in TFs_dict_query.items():
        idf = IDFs_dict_query[word]
        idf_2 = IDFs_dict_2_query[word]
        
        word_tfidf = TFIDF_Calculator.tfidf(tf, idf, max_freq)
        word_tfidf_2 = TFIDF_Calculator.tfidf(tf, idf_2, max_freq)
        TFIDFs_dict_query[word] = word_tfidf
        TFIDFs_dict_2_query[word] = word_tfidf_2
    
    return TFs_dict_query, TFIDFs_dict_query, TFIDFs_dict_2_query

def compute_similarity(document, query):  
        difference = 0
        for word, value in query.items():
            if word in document.keys():
                difference += abs(document[word] - value)
            else:
                difference += value
        if difference != 0:
            similarity = 1/difference
            return similarity
        else:
            return 0


def do_task_4(query_file, choice, resolution, file_no, window_length, stride):
    # wordified_query = task_1(query_file, resolution, file_no, window_length, stride)
    
    # TFs_dict_query, TFIDFs_dict_query, TFIDFs_dict_2_query = task_2(wordified_query)
        
    
    if choice == 1:
        with open('TF.txt', 'r') as f:
            documents = eval(f.read())
            # query = TFs_dict_query
            query = documents[file_no]
    elif choice == 2:
        with open('TFIDF.txt', 'r') as f:
            documents = eval(f.read())
            # query = TFIDFs_dict_query
            query = documents[file_no]
    elif choice == 3:
        with open('TFIDF_2.txt', 'r') as f:
            documents = eval(f.read())
            # query = TFIDFs_dict_2_query
            query = documents[file_no]
    else:
        print("Please enter either 1, 2, or 3 in the config file.")
        return None
    
    
    scores = {}
    for file_no, document in documents.items():
        score = compute_similarity(document, query)
        scores[file_no] = score
        
    results = [k for k, v in sorted(scores.items(), key=lambda item: item[1])][:10]
        
    print(results)
    time.sleep(5)
    return results


# results = do_task_4('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z/1.csv', 1, 3, 61, 3, 2)