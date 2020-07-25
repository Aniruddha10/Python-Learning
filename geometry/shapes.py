# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:39:45 2020

@author: chakanc
"""


pi = 3.14

def areaOfCircle(radius):
    return pi*(radius ** 2)

def areaAndPerimiter(length, width):
    area = length * width
    perimiter = 2 * (length+width)
    return area, perimiter