# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:30:06 2020

@author: chakanc
"""

def square(x):
    return x**2

def cube(x):
    return x**3

def sum(start, end, funct):
    total=0
    for i in range(start, end+1):
        total+=funct(i)
    return total


print(sum(3,5,square))
print(sum(3,5,cube))