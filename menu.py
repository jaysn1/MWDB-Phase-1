# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 02:48:41 2020

@author: Jaysn
"""

from consolemenu import *
from consolemenu.items import *
import config
from Normalizer import Normalizer

menu = ConsoleMenu("Phase 1")

function_item = FunctionItem("Task 1", 
                             Normalizer.get_normalized_files, 
                             args=[config.file_path, config.total_files])

selection_menu = SelectionMenu(["item1", "item2", "item3"])

submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

menu.append_item(function_item)
menu.append_item(submenu_item)

menu.show()
