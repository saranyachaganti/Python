# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:06:52 2019

@author: xinthe
"""

from utils.utils import read_arr

arr = read_arr()

pos_count = 0
neg_count = 0

for i in arr:
    if i >0:
        pos_count = pos_count+1
        
    else:
        neg_count = neg_count+1
        
print( pos_count, "   -   ", neg_count )
