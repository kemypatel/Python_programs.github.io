


import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 6
p =  "".join(random.sample(s,passlen ))
print('your generated password is ')
print (p)
