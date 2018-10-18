# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:10:34 2018

@author: kemy
"""

string = input("enter a string:")
if(string==string[::-1]):
    print("palindrome")
else:
    print("not palindrome")