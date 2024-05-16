#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

n = 600851475143
divisor = list()
i = 2

#search all divisor
while i <= math.sqrt(n):
    if n % i == 0:
        divisor.append(i)
    
    i += 1

print(divisor)

#check if divisor is a prime number
for div in divisor:
    for j in range(2, div //2):
        if div % j == 0:
            print(f"{div} not prime")
    

