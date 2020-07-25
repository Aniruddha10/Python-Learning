# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:43:28 2020

@author: chakanc
"""


import shapes as sp

def main():
    
    radius = 3
    length = -4
    width = 3
    
    try:
        
        print('Area of corcle withradis {} is {}'.format(radius,sp.areaOfCircle(radius)))

        area, perimiter = sp.areaAndPerimiter(length, width)
        print('Area and Perimiter of rectangle with length {} and width {} are {} and {}'.format(length,width,area, perimiter))
    except ValueError:
        print("Error in argument")
    finally:
        print("Execution complete")
