# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:52:21 2024

@author: sahil
"""

import numpy as np
from copy import copy
import bisect 
from collections import defaultdict
from itertools import product
from functools import reduce
from math import gcd


r_l = []
u_l = []
r_flag = True

with open('Q5.txt') as f:
    for line in f:
        line = line[:-1]
        if line == '':
            r_flag = False
            continue
        
        if r_flag:
            # Parse rules in the form 'a|b'
            a, b = map(int, line.split('|'))
            r_l.append((a, b))
        else:
            # Parse updates as lists of integers
            update = list(map(int, line.split(',')))
            u_l.append(update)

#print(r_l[:5])
#print(u_l[:5])

def is_good(u):
    #print(u)
    ui = {p:i for i,p in enumerate(u)}
    for a,b in r_l:
        if a in ui and b in ui:
            if ui[a] > ui[b]:
                return False
    return True

def fix(u):
    ui = {p:i for i,p in enumerate(u)}
    for a,b in r_l:
        if a in ui and b in ui:
            if ui[a] <= ui[b]:
                u[ui[a]], u[ui[b]] = u[ui[b]], u[ui[a]]
                return u
    return None

sum_1 = 0
sum_2 = 0

for u in u_l:
    if is_good(u):
        mi = len(u) // 2
        sum_1 += u[mi]
    else:
        #print(u)
        while fix(u) is not None:
            pass
        #print(u)
        mi = len(u) // 2
        sum_2 += u[mi]


print(sum_1)
print(sum_2)

