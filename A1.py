# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:12:53 2024

@author: sahil
"""

from collections import Counter

l_list, r_list = [], []
with open('Q1.txt') as f:
    for line in f:
        l, r = map(int, line[:-1].split())
        l_list.append(l)
        r_list.append(r)
        

sum_a = 0
sum_b = 0

right_count = Counter(r_list)
sorted_l, sorted_r = sorted(l_list), sorted(r_list)
for l, r in zip(sorted_l, sorted_r):
    sum_a += abs(l-r)


for l in l_list:
    sum_b += l*right_count[l]

print(sum_a)
print(sum_b)