# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:53:51 2018

@author: kemy
"""

a=[1,3,4,2,5,67,46,78,99]
b=[1,4,67,2,66,89,20,32,34,1]
c=[]
for i in b:
    if i in a:
        if i not in c:
            c.append(i)
            print(c)
