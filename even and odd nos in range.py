# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:01:13 2019

@author: saranya
"""

start = int(input ('enter starting number'))

end = int (input ('enter ending number'))

for num in range (start,end+1):
    if num %2 == 0 :
        print(num)
        
    else:
        print('not an even number')
