# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:48:41 2020

@author: Jaysn
"""

from consolemenu import *
from consolemenu.items import *
import config
import task_1_driver
import task_2_driver

menu = ConsoleMenu("Phase 1")

function_item_1 = FunctionItem("Task 1", 
                             task_1_driver.do_task_1, 
                             args=[config.file_path, config.normalized_file_path, config.quantized_file_path, config.word_file_path,
                                   config.total_files, config.resolution, config.window_length, config.stride])

function_item_2 = FunctionItem("Task2",
                               task_2_driver.do_task_2)


menu.append_item(function_item_1)
menu.append_item(function_item_2)

menu.show()
