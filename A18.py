# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 23:58:03 2024

@author: sahil
"""

from collections import deque

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start[0], start[1], 0)]) 
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == goal:
            return steps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and \
               0 <= ny < cols and \
               (nx, ny) not in visited and \
               grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    return -1 

def part_1(bytes_):
    rows, cols = 71, 71
    grid = [['.' for _ in range(cols)] for _ in range(rows)]  # Initialize the grid with safe cells

    for i in range(1024):
        x, y = bytes_[i]
        grid[x][y] = '#'

    start = (0, 0)
    goal = (70, 70)
    
    return bfs(grid, start, goal)


def part_2(bytes_):
    rows, cols = 71, 71
    grid = [['.' for _ in range(cols)] for _ in range(rows)]  # Initialize the grid with safe cells
    
    start = (0, 0)
    goal = (70, 70)
    
    for i in range(len(bytes_)):
        x, y = bytes_[i]
        grid[x][y] = '#'  
        
        if bfs(grid, start, goal) == -1:
            return x, y  
    
    return None


bytes_ = []

with open('Q18.txt') as f:
    for line in f:
        x,y = list(map(int, line[:-1].split(',')))
        bytes_.append((x,y))


result = part_1(bytes_)
print("Part 1:", result)

result = part_2(bytes_)
print(f"Part 2: {result[0]},{result[1]}")
