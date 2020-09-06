# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:48:41 2020

@author: Jaysn
"""

from consolemenu import *
from consolemenu.items import *
import config
import task_1_driver

menu = ConsoleMenu("Phase 1")

function_item = FunctionItem("Task 1", 
                             task_1_driver.do_task_1, 
                             args=[config.file_path, config.normalized_file_path, config.total_files, config.resolution])

selection_menu = SelectionMenu(["item1", "item2", "item3"])

submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

menu.append_item(function_item)
menu.append_item(submenu_item)

menu.show()
