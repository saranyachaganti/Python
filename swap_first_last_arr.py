# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:29:16 2019

@author: xinthe
"""

from utils.utils import read_arr

# define list 

arr = read_arr()

print(arr)

# Swap last and first elements

arr[-1], arr[0] = arr[0] , arr[-1]

print( arr)
