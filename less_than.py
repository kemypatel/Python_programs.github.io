# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:19:33 2018

@author: kemy
"""

a=[1,1,2,3,6,4,3,5,55,66,23,1,56]

print("all the elements are :")

print(a)

print("in the given list less than 5 are below:")
#b=[x<5 for x in a ]
#print(b)// use to print ture or false

x=[i for i in a if i <5]

print(x)



'''
output:
all the elements are :
[1, 1, 2, 3, 6, 4, 3, 5, 55, 66, 23, 1, 56]
in the given list less than 5 are below:
[1, 1, 2, 3, 4, 3, 1]
'''