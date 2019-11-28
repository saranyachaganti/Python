# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:34:19 2019

@author: xinthe
"""

def read_arr( d_type = int, stmt = "Enter the array" ) :
    
    in_arr = []
    
    print( stmt )

    while True:
        data_in = input()
        
        if data_in == '' :
            break
        if d_type == str :
            in_arr.append( str( data_in ))
        else :
            in_arr.append( int( data_in ) )
        
    return in_arr

def read_str (d_type = str, stmt = "enter the string"):
    in_str = str
    
    print( stmt )

    while True:
        data_in = input()
        
        if data_in == '' :
            break
        if d_type == str :
            in_str.append( str( data_in ))
        else :
            in_str.append( int( data_in ) )
        
from utils.utils import read_str


test = read_str()

print (test)