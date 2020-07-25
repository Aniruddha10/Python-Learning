# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:17:58 2020

@author: chakanc
"""

class ComplexNumber:
    def __init__(self,real,complex):
        self.real = real
        self.complex = complex
        
    def add(self, pnew):
        nreal = self.real + pnew.real
        ncomplex = self.complex+pnew.complex
        return ComplexNumber(nreal, ncomplex)
    
    def __str__(self):
        return format('{}+i{}'.format(self.real, self.complex))


#def main():
    