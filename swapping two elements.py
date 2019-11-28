# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:35:27 2019

@author: saranya
"""


from utils.utils import read_arr

# define list 

arr = read_arr()

print(arr)

# Swap last and first elements

def swapping(position1,position2,arr):

    arr[position1], arr[position2] = arr[position2] , arr[position1]
    
    return arr

print( swapping(1,2,arr) )
