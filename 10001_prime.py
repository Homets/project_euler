#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


#Sieve of Eratosthenes

result = 0

n = 4 #the nth prime number
i = 8
while n < 10001:
    prime = True
    div = math.floor(i / 2)
    for j in range(1,div + 1):
        if j > 1 and j < div and i % j == 0:
            prime = False
            #print(f"{i} IS NOT A PRIME NUMBER")

    if prime == True:
        print(f"{i} IS THE {n + 1}TH PRIME NUMBER")
        n += 1
        result = i
    i+= 1

print(result)
