# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:29:30 2019

@author: xinthe
"""

string = input("enter string")

string = string.split(' ')

for word in string:
    if len(word)%2==0 :
        print(word)

    