# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:46:11 2019

@author: xinthe
"""

from utils.utils import read_arr

# define array 

# take a temp element at the end of the array 

# replace arr[0] with the temp element 

# left and right shift



arr = []
arr = read_arr()
        
shift = int( input("Enter the rotation count") )

narr = arr

if shift > 0 :
    narr = arr[ shift : len(arr) ]
    narr.extend( arr[ 0 : shift ] )
elif shift < 0 :
    narr = arr[ 2-shift : len(arr) ]
    narr.extend( arr[ 0: 2 - shift ] )

print( narr )

        