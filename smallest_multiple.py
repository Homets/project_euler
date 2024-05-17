#!/usr/bin/env python
# -*- coding: utf-8 -*-
i = 20
num = 0
while (1):
    divided = True
    for j in range(1,20 + 1):
        if i % j != 0:
            divided = False
    if divided == True:
        num = i
        break
    i += 1

print(num)
