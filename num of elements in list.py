# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:22:48 2019

@author: saranya
"""

from utils.utils import read_arr
# read array
arr = read_arr()
key = int( input("Enter the key") ) 
# intialize count

def no_of_elem(arr,letter):
    counter = 0
    for n in arr:
        if (n == letter):
            counter = counter+1
    return counter 


# print
print(no_of_elem(arr,key))
