# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:22:11 2020

@author: chakanc
"""

class shape:
    def area(self):
        return 0

class square(shape):
    __length = 0
    def __init__(self, length):
        self.__length = length
    
    def area(self):
        return self.__length ** 2