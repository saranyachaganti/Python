# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:51:23 2019

@author: xinthe
"""

string = input("enter the string")

text = string.split(" ")

letter = input("enter the letter")

for i in text :
    if i == letter:
        text.strip(i)
        
    
else:
    pass

