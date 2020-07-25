# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:49:56 2020

@author: chakanc
"""

"Module:MathModul"
import MathStats as ms

print(ms.sum(3,5,ms.square))

def getFibanacci(number = 2):
    i = number
    sum=0
    while i>0:
        sum += i
        i+=-1
    return sum


def getTestResult(numberList):
    sum=0
    
    for score in numberList:
        sum+=score
        
    per = sum/len(numberList)
    grade=""
    if per > 50 :
        grade = "pass"
    else:
        grade="fail"
    return grade, per

n = 10
print('fibonacci of {} is {}'.format(n, getFibanacci(n)))    
print('fibonacci {}'.format(getFibanacci()))
g, p = getTestResult([60,60,50])
print(g)
print(p)    