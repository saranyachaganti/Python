# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:45:36 2019

@author: saranya
"""

from utils.utils import read_arr

arr = read_arr()

for i in arr :
    if i >0:
        print(i, 'is postiive')
        
    else:
        print(i ,' is negative')
