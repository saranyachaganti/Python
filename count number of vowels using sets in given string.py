# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:31:27 2019

@author: saranya
"""

string  =input("enter string")
counter = 0
vowel = set('aeiouAEIOU')

for alphabet in string:
    if alphabet in vowel:
        counter = counter+1
        
    else:
        pass

print(counter)
