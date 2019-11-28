# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:17:15 2019

@author: xinthe
"""

from utils.utils import read_arr

arr = read_arr()

arr_copy = arr[:] 

print(arr)
print(arr_copy)