# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:50:09 2019

@author: xinthe
"""

from utils.utils import read_arr

arr = read_arr()

for i in arr:
    if i%2 == 0:
        print ('even')
        
    else:
        print ('odd')