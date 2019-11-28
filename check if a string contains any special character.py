# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:06:00 2019

@author: xinthe
"""

string  =input("enter string")
valid_chars=['q','w','e','r','t','y','u','i','o','p','a','s','d','f',
             'g','h','j','k','l','z','x','c','v','b','n','m','Q','W',
             'E','R','T','Y','U','I','O','P','A','S','D','F','G','H',
             'J','K','L','Z','X','C','V','B','N','M','1','2','3','4',
             '5','6','7','8','9','0', ' ' ]

for i in string :
    if not ( i in valid_chars) :
        print("Contains special character -> ", i)
        #break
