# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:55:28 2024

@author: sahil
"""

from copy import deepcopy

def move_robot(warehouse, robot_position, move):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    robot_x, robot_y = robot_position
    dx, dy = directions[move]
    new_robot_x, new_robot_y = robot_x + dx, robot_y + dy

    if warehouse[new_robot_x][new_robot_y] == '#':
        return robot_position, warehouse 

    if warehouse[new_robot_x][new_robot_y] == 'O':
        is_free_space = False
        i = 1
        while True:
            tmp_x, tmp_y =  robot_x + i*dx, robot_y + i*dy
            if warehouse[tmp_x][tmp_y] == '.':
                is_free_space = True 
                break
            if warehouse[tmp_x][tmp_y] == '#':
                break
            i += 1
        
        
        if is_free_space:
            warehouse[tmp_x][tmp_y] = 'O'
            warehouse[new_robot_x][new_robot_y] = '@'
            warehouse[robot_x][robot_y] = '.'
            robot_position = new_robot_x, new_robot_y
        else:
            return robot_position, warehouse  # Can't push the box
    else:
        warehouse[new_robot_x][new_robot_y] = '@'
        warehouse[robot_x][robot_y] = '.'
        robot_position = new_robot_x, new_robot_y

    return robot_position, warehouse



def move_robot2(warehouse, robot_position, move):
    
    def _has_free_space(warehouse, x, y, dx, dy):
        i = 0
        #print(x,y,dx, dy)
        while True:
            tmp_x, tmp_y =  x + i*dx, y + i*dy
            if warehouse[tmp_x][tmp_y] == '.' :
                return True, tmp_x, tmp_y
            if warehouse[tmp_x][tmp_y] == '#':
                return False, tmp_x, tmp_y
            i+=1
    def _move_arr(warehouse, x, y, dx, dy, tmp_x, tmp_y):
        while (tmp_x,tmp_y) != (x,y):
            warehouse[tmp_x][tmp_y] = warehouse[tmp_x-dx][tmp_y-dy]
            tmp_x, tmp_y = tmp_x-dx, tmp_y-dy
        warehouse[x][y] = '.'
    
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    robot_x, robot_y = robot_position
    dx, dy = directions[move]
    new_robot_x, new_robot_y = robot_x + dx, robot_y + dy

    if warehouse[new_robot_x][new_robot_y] == '#':
        return robot_position, warehouse 

    if warehouse[new_robot_x][new_robot_y] in ['[' , ']']:
        
        if move in ['>', '<']:
            flg, tmp_x, tmp_y = _has_free_space(warehouse, robot_x, robot_y, dx, dy)
            if flg:
                _move_arr(warehouse, robot_x, robot_y, dx, dy, tmp_x, tmp_y)
            
        elif move in ['^', 'v']:
            
            j=0
            print_w(warehouse)
            starting_xys = [(robot_x, robot_y)]
            while True:
                tmp_x, tmp_y =  robot_x + j*dx, robot_y + j*dy
                if warehouse[tmp_x][tmp_y] == ']':
                    starting_xys.append( (tmp_x,tmp_y-1) )
                elif warehouse[tmp_x][tmp_y] == '[':
                    starting_xys.append( (tmp_x,tmp_y+1) )
                elif warehouse[tmp_x][tmp_y] == '#':
                    return robot_position, warehouse
                elif warehouse[tmp_x][tmp_y] == '.':
                    break
                j += 1
            for (x,y) in starting_xys:
                if not _has_free_space(warehouse, x, y, dx, dy):
                    return robot_position, warehouse
            for (x,y) in starting_xys:
                flg, tmp_x, tmp_y = _has_free_space(warehouse, x, y, dx, dy)
                _move_arr(warehouse, robot_x, robot_y, dx, dy, tmp_x, tmp_y)
            robot_position = new_robot_x, new_robot_y
    else:
        
        warehouse[new_robot_x][new_robot_y] = '@'
        warehouse[robot_x][robot_y] = '.'
        robot_position = new_robot_x, new_robot_y

    return robot_position, warehouse


def calculate_gps_sum(warehouse):
    gps_sum = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == 'O':
                gps_sum += 100 * i + j
    return gps_sum


def calculate_gps_sum2(warehouse):
    gps_sum = 0
    for x in range(len(warehouse)):
        for y in range(len(warehouse[0])):
            if warehouse[x][y] == '[':
                top_len = x
                left_len = y
                gps_box = 100 * top_len + left_len
                gps_sum = gps_sum + gps_box
    return gps_sum



def print_w(warehouse):
    for l in warehouse:
        print(''.join(l))

def simulate_robot_moves(warehouse, moves):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                robot_position = (i, j)
                break
    
    print_w(warehouse)
    for move in moves:
        
        robot_position, warehouse = move_robot(warehouse, robot_position, move)
        #print_w(warehouse)
        
    return calculate_gps_sum(warehouse)


def simulate_robot_moves2(warehouse, moves):
    warehouse = rescale_warehouse(warehouse)
    print_w(warehouse)
    
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                robot_position = (i, j)
                break

    for move in moves:
        robot_position, warehouse = move_robot2(warehouse, robot_position, move)
    return calculate_gps_sum2(warehouse)

def rescale_warehouse(warehouse):
    new_warehouse = []
    for row in warehouse:
        new_row = ''
        for tile in row:
            if tile == '#':
                new_row += '##'
            elif tile == 'O':
                new_row += '[]'
            elif tile == '.':
                new_row += '..'
            elif tile == '@':
                new_row += '@.'
        new_warehouse.append(list(new_row))
    return new_warehouse


warehouse = []
to_moves = False
moves = ''

with open('Q15t.txt') as f:
    for line in f:
        line = line[:-1]
        if len(line) == 0:
            to_moves = True
        if to_moves:
            moves += line
        else:
            warehouse.append(list(line))



result = simulate_robot_moves(deepcopy(warehouse), moves)
print("Sum of GPS coordinates:", result)



result = simulate_robot_moves2(deepcopy(warehouse), moves)
print("Sum of GPS coordinates:", result)
