# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:21:34 2019

@author: saranya
"""
  
def reverseWords(input): 
       
    inputWords = input.split(" ") 
 
    inputWords=inputWords[-1::-1] 
  
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'i have a bag'
    print (reverseWords(input) )
