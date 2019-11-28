# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:24:30 2019

@author: xinthe

"""

test_str = input("Enter the string")
i=int( input("Enter the position"))

new_str = test_str[0:i] + test_str[i+1:]

# Printing string after removal   
print ("The string after removal of i'th character : " + new_str) 

