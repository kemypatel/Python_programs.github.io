# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:29:31 2018

@author: kemy
"""
import random

num=random.randint(1,9)
guess=0
count=0

while guess !=num and guess!="exit":
    guess=input("what's your guess?")
    
    if guess=="exit":
        break
    
    guess=int(guess)
    count+=1
    
    if guess<num:
        print("to low!")
    elif guess>num:
        print("to high")
    else:
         print("You Won!")
         
    



