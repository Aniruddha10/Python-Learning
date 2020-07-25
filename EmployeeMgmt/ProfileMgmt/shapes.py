# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:39:45 2020

@author: chakanc
"""


pi = 3.14

def areaOfCircle(radius):
    if radius < 0:
        raise ValueError("radius cannot be negative")
   
    return pi*(radius ** 2)

def areaAndPerimiter(length, width):
    if length <0 or width <0:
        raise ValueError("length or width cannot be negative")
    
    area = length * width
    perimiter = 2 * (length+width)
    return area, perimiter