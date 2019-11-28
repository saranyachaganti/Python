# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:14:34 2019

@author: xinthe
"""

big_string = input('enter big string')
small_string = input('enter small string')

for i in range(0, len(big_string) - len(small_string) + 1 ) :
    
    if ( big_string[i:i+len(small_string)] == small_string ) :
        print( " exists at position ", i)
        break
    

       
