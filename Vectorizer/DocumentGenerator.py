# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:03:49 2020

@author: Jaysn
"""
from tqdm import tqdm

def get_documents(WORD_FILE_PATH, total_files):
    documents_sensor_wise_dict = {}
    
    for file_no in tqdm(range(1, total_files+1)):
        file_name = '{0}/{1}.wrd'.format(WORD_FILE_PATH, file_no)
        with open(file_name, 'r') as word_file:
            gesture_words = word_file.read()
        gesture_words = eval(gesture_words)
        for sensor_id in range(len(gesture_words)):
            sensor_gesture_words = list(map(lambda x: x[1], gesture_words[sensor_id]))
            if file_no == 1:
                documents_sensor_wise_dict[sensor_id+1] = [sensor_gesture_words]
            else:
                documents_sensor_wise_dict[sensor_id+1].append(sensor_gesture_words)
    
    return documents_sensor_wise_dict

def get_documents_2(WORD_FILE_PATH, total_files):
    documents_gesture_wise_dict = {}
    
    for file_no in tqdm(range(1, total_files+1)):
        file_name = '{0}/{1}.wrd'.format(WORD_FILE_PATH, file_no)
        with open(file_name, 'r') as word_file:
            gesture_words = word_file.read()
        gesture_words = eval(gesture_words)
        
        for sensor_id in range(len(gesture_words)):
            sensor_gesture_words = list(map(lambda x: x[1], gesture_words[sensor_id]))
            if sensor_id == 0:
                documents_gesture_wise_dict[file_no] = [sensor_gesture_words]
            else:
                documents_gesture_wise_dict[file_no].append(sensor_gesture_words)
    
    return documents_gesture_wise_dict
        