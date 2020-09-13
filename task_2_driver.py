# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:11:48 2020

@author: Jaysn
"""
from tqdm import tqdm
from Vectorizer import DocumentGenerator
from Vectorizer import TF_Calculator
from Vectorizer import IDF_Calculator
from Vectorizer import TFIDF_Calculator

def save_vectors_file(documents_gesture_wise_dict, TFs_dict, TFIDFs_dict, TFIDFs_dict_2, VECTOR_FILE_PATH, total_files):
    for file_no in tqdm(range(1, total_files+1)):
        file_name = '{0}/vectors_{1}.txt'.format(VECTOR_FILE_PATH, file_no)
        TFs = TFs_dict[file_no]
        TFIDFs = TFIDFs_dict[file_no]
        TFIDF_2s = TFIDFs_dict_2[file_no]
        
        vectors = []
        for sensor_id, sensor_words in enumerate(documents_gesture_wise_dict[file_no]):
            vector = []
            TF = TFs[sensor_id]
            TFIDF = TFIDFs[sensor_id]
            TFIDF2 = TFIDF_2s[sensor_id]
            for word in sensor_words:
                word_vector = [TF[word], TFIDF[word], TFIDF2[word]]
                vector.append(word_vector)
            vectors.append(vector)
        
        with open(file_name, 'w+') as file:
            file.write(str(vectors))
        
        
def do_task_2(WORD_FILE_PATH, VECTOR_FILE_PATH, total_files):
    print("\nGetting document words dictionary (sensor wise)...")
    documents_sensor_wise_dict = DocumentGenerator.get_documents(WORD_FILE_PATH, total_files)
    
    print("\nGetting document words dictionary (gesture wise)...")
    documents_gesture_wise_dict = DocumentGenerator.get_documents_2(WORD_FILE_PATH, total_files)
    
    print("\nGetting Term Frequencies...")
    TFs_dict = TF_Calculator.calculate_TF(WORD_FILE_PATH, total_files)
    
    print("\nGetting IDFs...")
    IDFs_dict = IDF_Calculator.calculate_IDF(documents_sensor_wise_dict, total_files)
    
    print("\nGetting IDFs 2...")
    IDFs_dict_2 = IDF_Calculator.calculate_IDF2(documents_gesture_wise_dict, total_files)
    
    print("\nCalculating TF-IDFs...")
    TFIDFs_dict = TFIDF_Calculator.calculate_TFIDF(TFs_dict, IDFs_dict)
    
    print("\nCalculating TF-IDF2s...")
    TFIDFs_dict_2 = TFIDF_Calculator.calculate_TFIDF_2(TFs_dict, IDFs_dict_2)
    
    print("\nSaving Vectors...")
    save_vectors_file(documents_gesture_wise_dict, TFs_dict, TFIDFs_dict, TFIDFs_dict_2, VECTOR_FILE_PATH, total_files)
    
    
    
    # return documents_sensor_wise_dict, documents_gesture_wise_dict, TFs_dict, IDFs_dict, IDFs_dict_2, TFIDFs_dict, TFIDFs_dict_2 
    
# documents_sensor_wise_dict, documents_gesture_wise_dict, TFs_dict, IDFs_dict, IDFs_dict_2, TFIDFs_dict, TFIDFs_dict_2 = do_task_2('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Word_Files', 'C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Vectors', 60)