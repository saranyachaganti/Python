# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:43:29 2019

@author: saranya
"""

from utils.utils import read_arr

#read list
arr = read_arr(d_type=str)

narr = []

def is_str_exists(arr, wrd):
    
    for word in arr:
        if word == wrd :
            return True
        
    return False

print(arr)    
# loop to match every word 
for word in arr :
    
    if not is_str_exists( narr, word ) :
        narr.append(word)
        
arr = narr

print( narr )   
