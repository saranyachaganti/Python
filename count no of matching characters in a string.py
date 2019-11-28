# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:08:05 2019

@author: xinthe
"""

def cnt_char_str(str1, c1) :
    cnt = int(0)
    
    for i in str1 :
        if i == c1 :
            cnt=cnt+1
    
    return cnt


string1 = input("enter the string 1")
string2 = input("enter the string 2")

listed_chars = []

for c in string1 + string2  :
    if ( c in string1 ) and ( c in string2 ) and not (c in listed_chars):
        cnt = cnt_char_str( string2, c)
        if cnt > 0 :
            print( c, " -> ", cnt )

    listed_chars.append(c)
    
    




        

