# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:00:59 2020

@author: Jaysn
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def get_data_for_viz(file_path, file_choice, choice):
    file_name = '{0}/vectors.txt'.format(file_path)
    with open(file_name, 'r') as file:
        data = eval(file.read())
        
    data = data[file_choice]
    
    TFs = []
    TFIDFs = []
    TFIDF_2s = []
    
    if choice == 1:
        for row in data:
            TF = [vector[0] for vector in row]
            TFs.append(TF)
        return TFs
    elif choice == 2:
        for row in data:
            TFIDF = [vector[1] for vector in row]
            TFIDFs.append(TFIDF)
        return TFIDFs
    elif choice == 3:
        for row in data:
            TFIDF_2 = [vector[2] for vector in row]
            TFIDF_2s.append(TFIDF_2)
        return TFIDF_2s
    else:
        print("Please enter either 1, 2, or 3 in the config file.")
        return None

def normalize(data):
    MINIMUM_VALUE = 0
    MAXIMUM_VALUE = 255
    data = np.array(data)
    minimum = np.min(data)
    maximum = np.max(data)
    normalized_data = []
    for i in range(len(data)):
        norm_temp = list(map(lambda x: MINIMUM_VALUE + ((MAXIMUM_VALUE - MINIMUM_VALUE) * (x - minimum) / (maximum - minimum)), data[i]))
        normalized_data.append(norm_temp)
    return normalized_data

def create_heatmap(data): 
    data = normalize(data)
    # plt.imshow(data, cmap='gray')
    # plt.show()
    sns.heatmap(data, cmap='gray', yticklabels=(range(1,21)))
    plt.show()

def do_task_3(file_path, file_choice, choice):
    data = get_data_for_viz(file_path, file_choice, choice)
    create_heatmap(data)
    return data
    
# data = do_task_3('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Z', 1, 1)