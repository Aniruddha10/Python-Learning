# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:32:28 2020

@author: chakanc
"""

class Project:
    
    
class Empployee(Project):
    __Id = ""
    __name = ""
    __age = 0
    __salary = 0.00
    
    def __init__(self, id, name, age, salary):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__salary = salary
        
    def Save(self):
        # Write To File
    
    def Get(self, id):
        # Get from file