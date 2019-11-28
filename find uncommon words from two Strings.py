# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:06:27 2019

@author: saranya
"""

str1 = input("enter string")

str2 = input("enter string")

for word  in ( str1 + " " + str2).split(" "):
    if not ( word in str1.split(" ") and word in str2.split(" ")) :
        print(word)
        
