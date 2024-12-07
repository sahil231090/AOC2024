# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:53:36 2024

@author: sahil
"""

from itertools import product

lines = []

t_list = []
n_arr_list = []
with open('Q7.txt') as f:
    for line in f:
        
        line = line[:-1]
        
        lines.append(list(line))
        
        t_str, n_arr_list_str = line.split(":")
        
        t = int(t_str.strip())
        n_arr = list(map(int, n_arr_list_str.strip().split()))
        
        t_list.append(t)
        n_arr_list.append(n_arr)
        

#print(t_list)
#print(n_arr_list)


def run(n_arr, o_arr):
    #print(n_arr, o_arr)

    s = n_arr[0]
    for n, o in zip(n_arr[1:], o_arr):
        
        if o == '+':
            s += n
        elif o == '*':
            s *= n
        elif o == '||':
            # Concatenate the numbers as strings and convert back to integer
            s = int(str(s) + str(n))
    return s


def check_eq(n_arr, t, eqs):
    n = len(n_arr)
    o_arr_list = product(eqs, repeat=n-1)
    
    for o_arr in o_arr_list:
        if run(n_arr, o_arr) == t:
            return True
    return False

sum_1 = 0
sum_2 = 0
for t, n_arr in zip(t_list, n_arr_list):
    if check_eq(n_arr, t, eqs=['+', '*']):
        sum_1 += t
    if check_eq(n_arr, t, eqs=['+', '*', '||']):
        sum_2 += t
print(sum_1)
print(sum_2)




