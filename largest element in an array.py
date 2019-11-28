# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:15:18 2019

@author: xinthe
"""

from utils.utils import read_arr

# define an array 

#   Store the first element into a variable v

#   Loop through the elements and copy the element into v
#   if the element is greater than the element in v


arr = read_arr()

maxv = arr[0]

for val in arr:
    
    if val > maxv :
        maxv = val
    
print("max is ", maxv)


