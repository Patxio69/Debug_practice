import random, math, os

def number_gen():
    print("type your range")
    n = input("here")
    print("how long?")
    ranger = input()
    for looper in range(int(ranger)):
        password_str = random.randint(0, int(n))
        return password_str


def random_num():               #second code here
    num = random.randint(0, 100)
    for e in range(10):
        return ("random" + str(num))
        

#for something in range(int(how)):
something = random_num()
print(something)


import random  #infilately loops the random values

def random_num():
    num = random.randint(0, 100)
    for e in range(10):
        return ("random" + str(num))
        
while True:
    print(random_num())

import random
amount = 30
print(random.randint(10**(amount-1), (10**amount)-1))
