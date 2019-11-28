# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:48:27 2019

@author: xinthe
"""

#from utils.utils import read_arr

start = int(input ('enter starting point'))
end = int(input ('enter ending point'))

for i in range(start,end):
    if i>0:
        print('positive')
    else:
        print('negative')