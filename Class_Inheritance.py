# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:56:59 2020

@author: ramoj
"""

class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def __str__(self):
    return 'point : ({}, {}, {})'.format(self.x, self.y, self.z)
 
    
p1 = Point(4, 2, 9) 
print(p1)        
