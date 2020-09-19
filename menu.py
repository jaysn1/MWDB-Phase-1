# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:48:41 2020

@author: Jaysn
"""

from consolemenu import *
from consolemenu.items import *
import time
import config
import task_1_driver
import task_2_driver
import task_3_driver
import task_4_driver



def run_all_tasks():
    task_1_driver.do_task_1(config.file_path, config.normalized_file_path, config.quantized_file_path, config.word_file_path,
                                   config.total_files, config.resolution, config.window_length, config.stride)
    task_2_driver.do_task_2(config.word_file_path, config.vector_file_path, config.total_files)
    task_3_driver.do_task_3(config.vector_file_path, config.file_choice, config.visualization_choice)
    task_4_driver.do_task_4(config.query_file, config.similarity_choice, config.resolution, config.query_file_no, 
                                     config.window_length, config.stride)
    print("Ran all tasks")
    time.sleep(2)


menu = ConsoleMenu("Phase 1")

function_item_1 = FunctionItem("Run Task 1", 
                             task_1_driver.do_task_1, 
                             args=[config.file_path, config.normalized_file_path, config.quantized_file_path, config.word_file_path,
                                   config.total_files, config.resolution, config.window_length, config.stride])

function_item_2 = FunctionItem("Run Task 2", 
                               task_2_driver.do_task_2,
                               args=[config.word_file_path, config.vector_file_path, config.total_files])


function_item_3 = FunctionItem("Run Task 3",
                               task_3_driver.do_task_3,
                               args=[config.vector_file_path, config.file_choice, config.visualization_choice])

function_item_4 = FunctionItem("Run Task 4",
                               task_4_driver.do_task_4,
                               args=[config.query_file, config.similarity_choice, config.resolution, config.query_file_no, 
                                     config.window_length, config.stride])

function_item_5 = FunctionItem("Run all tasks",
                               run_all_tasks)


menu.append_item(function_item_1)
menu.append_item(function_item_2)
menu.append_item(function_item_3)
menu.append_item(function_item_4)
menu.append_item(function_item_5)

menu.show()

