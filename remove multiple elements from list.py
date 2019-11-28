# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:09:53 2019

@author: saranya
"""

arr = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
                  ('krishna', 'akbar', '45'), ('',''),()]
   
for l in arr:
    if not l :
          arr.remove(l) 
    

print(arr)    
