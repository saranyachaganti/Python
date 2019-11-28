# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:46:42 2019

@author: saranya
"""

from utils.utils import read_arr
  
arr = []
arr = read_arr()

n = int(input('enter N value :'))

length = len(arr)
print(length)



def output(length,arr,n):
    m = 1
    for i in range(length):  
        m = (m * (arr[i]))
    return m % n

print( "output is ", output(length, arr, n ))
