# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:14:40 2018

@author: kemy
"""

num = int(input("Enter a number :"))
if num >1:
    for i in range(2,num):
        if (num%i)==0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("is not prime")