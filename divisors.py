# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:51:11 2018

@author: kemy
"""

num = int(input("Please enter number :"))
list_divisors = []

for i in range(1, num):
    if num % i ==0:
        list_divisors.append(i)
print(list_divisors)