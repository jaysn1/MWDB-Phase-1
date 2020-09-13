# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:00:59 2020

@author: Jaysn
"""
import matplotlib.pyplot as plt
import seaborn as sns

def get_data_for_viz(file_path, choice):
    with open(file_path, 'r') as file:
        data = eval(file.read())
    TFs = []
    TFIDFs = []
    TFIDF_2s = []
    
    if choice == 1:
        for row in data:
            TF = [vector[0] for vector in row]
            TFs.append(TF)
        print(data)
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


def create_heatmap(data):
    plt.imshow(data, cmap='gray')
    # sns.heatmap(data)

def do_task_3(file_path, choice):
    data = get_data_for_viz(file_path, choice)
    create_heatmap(data)
    return data
    
data = do_task_3('C:/Users/Jaysn/Anaconda3/envs/MWDB_Phase_1/src/Data/Vectors/vectors_1.txt', 1)