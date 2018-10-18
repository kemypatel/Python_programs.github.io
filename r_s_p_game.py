# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:16:30 2018

@author: kemy
"""
from random import randint

player=input("rock (r),paper(p),scissors(s)?")

print(player,"vs ",end='')

chosen=randint(1,3)
#print(chosen)

if chosen==1:
    computer='r'
elif chosen==2:
    computer='p'
else:
    computer='s'
print(computer)

if player==computer:
    print("DRAW!")
elif player=='r' and computer=='s':
    print("Player wins!")
elif player=='r' and computer=='p':
    print("Computer wins!")
elif player=='p' and computer=='r':
    print("player wins!")
elif player=='p' and computer=='s':
    print("computer wins!")    
    