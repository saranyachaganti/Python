# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:49:37 2019

@author: saranya
"""       
        
def check(string) : 

    vowels = set("aeiou") 

    s = set({}) 

    for char in string : 

        if char in vowels : 
            s.add(char) 
        else: 
            pass

    if len(s) == len(vowels) : 
        print("Accepted") 
    else : 
        print("Not Accepted") 
  
  
# Driver code 
if __name__ == "__main__" : 
      
    string = "SEEquoiaL"
  
    # lower method of string convert 
    # every character into small letter 
    string = string.lower() 
  
    # calling function 
    check(string) 
