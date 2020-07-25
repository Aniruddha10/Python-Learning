# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:21:45 2020

@author: chakanc
"""

def readFile(fileName):
    if fileName == "":
        raise FileNotFoundError("File not found")
    try:
        print("Hello")
    except FileNotFoundError as ex:
        print("error found")
        print(ex)

def divide(dividend, divisior):
    result = 0
    error = finalmessage = ""
    try:
        result = dividend/divisior
    except ZeroDivisionError:
        error = "cannot divide by error"
    finally:
        finalmessage = "execution complete"
        
    return result, error, finalmessage


result, error, finalmessage = divide(4,2)
print('Division result {}'.format(result))
print("Error "+ error)
print("Final Message "+ finalmessage)

readFile("")