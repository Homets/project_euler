#!/usr/bin/env python
# -*- coding: utf-8 -*-

#the sum of the square 1² + 2²+...
sum_square = 0
for i in range(1,100 + 1):
    sum_square += i*i

#the square of the sums (1 + 2 + 3+...)²
square_sum = 0
for i in range(1,100 + 1):
    square_sum += i
square_sum *= square_sum

print(square_sum - sum_square)
