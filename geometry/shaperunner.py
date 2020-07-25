# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:43:28 2020

@author: chakanc
"""


import shapes as sp

def main():
    
    radius = 5
    print('Area of corcle withradis {} is {}'.format(radius,sp.areaOfCircle(5)))

    length = 4
    width = 3
    area,perimiter = sp.areaAndPerimiter(length, width)
    print('Area and Perimiter of rectangle with length {} and width {} are {} and {}'.format(length,width,area, perimiter))
    
main()