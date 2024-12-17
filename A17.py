# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 23:54:34 2024

@author: sahil
"""


from copy import deepcopy

def run_program(registers, program):
    A, B, C = registers
    ip = 0
    output = []
    
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        
        def get_combo_operand(operand, A,B,C):
        
            if operand == 0:
                return 0
            elif operand == 1:
                return 1
            elif operand == 2:
                return 2
            elif operand == 3:
                return 3
            elif operand == 4:
                return A
            elif operand == 5:
                return B
            elif operand == 6:
                return C
            else:
                return None
            
        combo_operand = get_combo_operand(operand, A,B,C)
        ip += 2
        
        if opcode == 0:  # adv
            denominator = 2 ** combo_operand
            A = A // denominator
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = combo_operand % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            output.append(combo_operand % 8)

        elif opcode == 6:  # bdv
            denominator = 2 ** combo_operand
            B = A // denominator
        elif opcode == 7:  # cdv
            denominator = 2 ** combo_operand
            C = A // denominator
    
    return output

registers = [55593699, 0, 0]
program = [2,4,1,3,7,5,0,3,1,5,4,4,5,5,3,0]


result = run_program(registers, program)
print('Part 1')
print(",".join(map(str, result)))



def find_A_6(program):
    A = 1
    while True:
        output = run_program([A, 0, 0], program)
        
        # Check if the output matches the program
        if output == program:
            return A
        
        if output[-6:] == program[-6:]:
            return A

        A += 1

# 393 -- last 3
# 3145 -- last 4
# 25420 -- last 5 [6, 1, 5, 1, 4]
# 220294 -- last 6  [6, 5, 6, 2, 0, 6]
# 1762354 -- last 7 [6, 5, 6, 2, 0, 6, 2]

initial_A = find_A_6(program)

offset = 7
while offset <= len(program):
    tmpA = initial_A*8
    
    while True:
        
        output = run_program([tmpA, 0, 0], program)
        if output[-offset:] == program[-offset:]:
            #print(tmpA, offset)
            break
        
        tmpA+=1
    
    initial_A = deepcopy(tmpA)
    offset+=1
    

result = run_program([initial_A,0,0], program)
print('Part 2')
print(initial_A)
