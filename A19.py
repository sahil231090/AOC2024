# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 00:41:34 2024

@author: sahil
"""


import numpy as np
from copy import copy
import bisect 
from collections import defaultdict
from itertools import product
from functools import reduce
from math import gcd


designs = []
with open('Q19.txt') as f:
    for idx, line in enumerate(f):
        line = line[:-1]
        if idx == 0:
            patterns = list(map(lambda x: x.strip(), line.split(',')))
        if idx > 1:
            designs.append(line)
            
            
def can_form_design(design, patterns):
    dp = [False] * (len(design) + 1)
    dp[0] = True
    
    for i in range(len(design)):
        if dp[i]:
            for pattern in patterns:
                if design[i:i + len(pattern)] == pattern:
                    dp[i + len(pattern)] = True
    
    return dp[len(design)]


def count_ways_to_design(design, patterns):
    dp = [0] * (len(design) + 1)
    dp[0] = 1
    
    for i in range(len(design)):
        if dp[i] > 0:
            for pattern in patterns:
                if design[i:i + len(pattern)] == pattern:
                    dp[i + len(pattern)] += dp[i]  
    
    return dp[len(design)]




possible_count = 0; total_ways = 0

for design in designs:
    if can_form_design(design, patterns):
            possible_count += 1
    total_ways += count_ways_to_design(design, patterns)
    
print(possible_count)
print(total_ways)



