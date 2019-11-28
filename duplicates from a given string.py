# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:31:32 2019

@author: saranya
"""

def cnt_char_str(str1, c1) :
    cnt = int(0)
    
    for i in str1 :
        if i == c1 :
            cnt=cnt+1
    
    return cnt

s1 = input("enter string")
listed_chars = []

for c in s1 :
    if  not ( c in listed_chars) and ( cnt_char_str( s1, c ) > 1 ) :
        print( c )
    listed_chars.append(c)
        
        
