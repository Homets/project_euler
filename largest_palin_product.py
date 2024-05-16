#!/usr/bin/env python
# -*- coding: utf-8 -*-


product_a = 999
max_pal = 0
pal_find = False

## check product_a (999) with all number in decreasing order
## if no palindrome is found decrement product_a
## 
while product_a > 0:
    for i in reversed(range(1,999 + 1)):
        num = product_a * i

        #reverse the num
        num_copy = num #get a copy because we will divide this number by 10
        rev = 0
        while num_copy > 0:
            rev = rev * 10 + num_copy % 10
            num_copy //= 10
        
        if rev == num:
            if max_pal < num:
                max_pal = num

    product_a -= 1

print(f"MAX_PAL={max_pal}")
    
