# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:49:02 2019

@author: saranya
"""

def returnSum(dict): 
      
     sum = 0
     for i in dict.values(): 
           sum = sum + i 
       
     return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 
