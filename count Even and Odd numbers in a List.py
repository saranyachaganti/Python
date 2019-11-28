# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:39:58 2019

@author: saranya
"""

from utils.utils import read_arr

arr = read_arr()

even_count = 0
odd_count = 0

for i in arr:
    if i %2==0:
        even_count = even_count+1
        
    else:
        odd_count = odd_count+1
        
print( even_count, "   -   ", odd_count )
