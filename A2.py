# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:34:38 2024

@author: sahil
"""

import numpy as np
from copy import copy
import bisect 
from collections import defaultdict
from itertools import product
from functools import reduce
from math import gcd

lines = []
arr_l = []
i = 0
with open('Q2.txt') as f:
    for line in f:
        lines.append(line[:-1])
        arr_l.append(np.array(list(map(int, line[:-1].split()))))
        i = i + 1

def _is_safe(l):
    
    if np.all(np.diff(l) <= 3) and np.all(np.diff(l) >= 1):
        return 1
    if np.all(np.diff(l) <= -1) and np.all(np.diff(l) >= -3):
        return 1
    return 0

    

s_c = 0
s_c2 = 0
for l in arr_l:
    s_c += _is_safe(l)
    n = len(l)
    for idx, e in enumerate(l):
        if idx == 0:
            l2 = l[idx+1:]
        elif idx == n-1:
            l2 = l[:idx]
        else:
            l2=np.append(l[:idx], l[idx+1:])
        res = _is_safe(l=l2)
        s_c2 += res
        if res == 1:
            break

        
print(s_c)
print(s_c2)

