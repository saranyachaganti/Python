# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:04:32 2019

@author: xinthe
"""

total = 0
  
# creating a list 

from utils.utils import read_arr
# read array
arr = read_arr() 
  
# Iterate each element in list 
# and add them in variale total 
for ele in range(0, len(arr)): 
    total = total + arr[ele] 
  
# printing total value 
print(total) 