# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:14:24 2019

@author: saranya
"""

string  =input("enter string")
length = int(input("enter length"))

text = string.split(" ") 

#print(text)
for i in text :
    if len(i) == length:
        print(i)
        
    else:
        pass
    
