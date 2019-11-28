# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:39:35 2019

@author: xinthe
"""

# Sum of elements of an array 
# Declare an array variable
arr = []
# Read the elements of the array
while True :
    i = input()
    if i == '' :
        break
    arr.append(i)
    
print(arr)

# find length of arrayv 
#leng = len(arr)

#print(leng)

#   Initialize a sum variable
sum = 0

#   Loop through the elements of the array and add them
#   to a variable
for i in arr:
    sum += int( i )
    

#   display sum value
print(sum)

