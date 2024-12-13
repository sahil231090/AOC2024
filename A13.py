# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:55:40 2024

@author: sahil
"""

import numpy as np

def min_tokens_to_win(prizes):
    total_tokens = 0
    total_prizes_won = 0
    prize_tf = [False]*len(prizes)

    for idx,prize in enumerate(prizes):
        X_a_move, Y_a_move, X_b_move, Y_b_move, prize_x, prize_y = prize
        min_cost = float('inf')

        for A in range(101):
            for B in range(101):
                if A * X_a_move + B * X_b_move == prize_x and A * Y_a_move + B * Y_b_move == prize_y:
                    cost = 3 * A + B
                    min_cost = min(min_cost, cost)
        
        if min_cost != float('inf'):
            total_tokens += min_cost
            total_prizes_won += 1
            prize_tf[idx]=True

    return total_prizes_won, total_tokens, prize_tf



def min_tokens_to_win2(prizes, adjustment = 10000000000000):
    total_tokens = 0
    total_prizes_won = 0
    prize_tf = [False]*len(prizes)

    for idx, prize in enumerate(prizes):
        X_a_move, Y_a_move, X_b_move, Y_b_move, prize_x, prize_y = prize
        prize_x, prize_y = prize_x+adjustment, prize_y+adjustment

        A_matrix = np.array([[X_a_move, X_b_move],
                             [Y_a_move, Y_b_move]])
        
        B_matrix = np.array([prize_x, prize_y])

        # Solve the system 
        solution = np.linalg.solve(A_matrix, B_matrix)
        

        A = int(np.round(solution[0])) 
        B = int(np.round(solution[1]))
   
        # verify int sol
        if not( A * X_a_move + B * X_b_move == prize_x and A * Y_a_move + B * Y_b_move == prize_y ):
            continue
        if A<0:
            continue
        if B<0:
            continue
        
        
        cost = 3 * A + B
        total_tokens += cost
        total_prizes_won += 1
        prize_tf[idx] = True
                
    return total_prizes_won, total_tokens, prize_tf

filename = 'Q13.txt'

prizes = []

with open(filename, 'r') as file:
    lines = file.readlines()
lines = list(filter(lambda x: len(x)>5, lines))


for i in range(0, len(lines), 3):
    # print(lines[i], lines[i+1])
    button_a = list(map(lambda x: int(x.split('+')[-1]), lines[i][:-1].split(': ')[-1].strip().split(', ')))
    button_b = list(map(lambda x: int(x.split('+')[-1]), lines[i+1][:-1].split(': ')[-1].strip().split(', ')))
    prize = list(map(lambda x: int(x.split('=')[-1]), lines[i+2][:-1].split(': ')[-1].strip().split(', ')))
    
    X_a_move, Y_a_move = button_a
    X_b_move, Y_b_move = button_b
    prize_x, prize_y = prize
    
    prizes.append((X_a_move, Y_a_move, X_b_move, Y_b_move, prize_x, prize_y))


# Solve the problem
prizes_won, tokens_spent, prize_tf = min_tokens_to_win(prizes)
print(f"Part 1: Prizes won: {prizes_won}, Tokens spent: {tokens_spent}")

prizes_won, tokens_spent, prize_tf = min_tokens_to_win2(prizes, adjustment=10_000_000_000_000)
print(f"Part 2: Prizes won: {prizes_won}, Tokens spent: {tokens_spent}")
