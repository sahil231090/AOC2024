# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:54:38 2024

@author: sahil
"""
from collections import Counter

def blink(stone):
    if stone == 0:
        return [1]
    
    num_digits = 0
    temp = stone
    while temp > 0:
        num_digits += 1
        temp //= 10

    if num_digits % 2 == 0:
        mid = num_digits // 2
        left = stone // (10 ** mid)
        right = stone % (10 ** mid)
        return [left, right]
    else:
        return [stone * 2024]

def calc(initial_stones, num_blinks):
    # Init
    stone_counter = Counter(initial_stones)
    
    for _ in range(num_blinks):
        # New
        new_counter = Counter()
        
        for stone, count in stone_counter.items():
            transformed_stones = blink(stone)
            
            #Merge
            for transformed in transformed_stones:
                new_counter[transformed] += count
        # Update
        stone_counter = new_counter
    
    return sum(stone_counter.values())

initial_stones = [9759, 0, 256219, 60, 1175776, 113, 6, 92833]

print(f"Number of stones after 25 blinks: {calc(initial_stones, 25)}")
print(f"Number of stones after 75 blinks: {calc(initial_stones, 75)}")
