# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:46:42 2019

@author: xinthe
"""

from utils.utils import read_arr
  
# define an array 

# multiply all the contents of an array 

# divide trhem by a number n 

# print the value 

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
