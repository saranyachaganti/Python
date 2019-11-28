# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:37:41 2019

@author: xinthe
"""

import random
import string

def gen_rand_str( length ) :
    
    chars = list(string.ascii_letters + string.digits)
    
    return ''.join(random.choice(chars) for i in range(length ) )


s1 = input("Enter the string")

cnt = 0

while True :
    
    #s2 = gen_rand_str( ( list( s1 ) ))
    s2 = gen_rand_str( len(s1) ) 
    
    cnt = cnt + 1
    
    if not s1 == s2 :
        
        print( s2 )
        
    else :
        print("Found ", s2, " at ", cnt)
        break
    
