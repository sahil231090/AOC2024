# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:54:20 2024

@author: sahil
"""



directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

######################
## Part 1
######################


# borrowed from https://www.datacamp.com/tutorial/breadth-first-search-in-python
def bfs(grid, start_x, start_y):
    from collections import deque

    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    reachable_nines = 0
    
    while queue:
        x, y = queue.popleft()
        
        # Check if we've reached a '9'
        if grid[x][y] == 9:
            reachable_nines += 1
        
        # Try to move in all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:  # Hiking trail condition
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return reachable_nines

def total_score(grid):
    total = 0
    rows, cols = len(grid), len(grid[0])
    
    # Loop through each position in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:  # Found a trailhead
                total += bfs(grid, i, j)  # Get the score for this trailhead
                
    return total


######################
## Part 2
######################



# Borrowed from stackoverflow
class TreeNode:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)



def dfs(grid, x, y, parent_node, visited):
    rows, cols = len(grid), len(grid[0])
    # Check all 4 possible directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
            if grid[nx][ny] == grid[x][y] + 1:
                visited.add((nx, ny))
                child_node = TreeNode(nx, ny, grid[nx][ny])
                parent_node.add_child(child_node)
                dfs(grid, nx, ny, child_node, visited)
                visited.remove((nx, ny))


def build(grid):
    rows, cols = len(grid), len(grid[0])
    all_trails = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:  # Found a trailhead
                visited = set([(i, j)])
                root_node = TreeNode(i, j, 0)
                dfs(grid, i, j, root_node, visited)
                all_trails.append(root_node)

    return all_trails



def count_leaf(node):
    if not node.children and node.h ==9:
        return 1
    total = 0
    for child in node.children:
        total += count_leaf(child)
    return total


def total_count(grid):
    all_trails = build(grid)
    score = 0
    for root in all_trails:
        #print("Head at:", f"({root.x}, {root.y})")
        tmp = count_leaf(root)
        score += tmp
    return score    



######################
## Solution
######################


grid = []
with open('Q10t.txt') as f:
    for line in f:        
        line = line[:-1]        
        grid.append(list(map(lambda x: int(x) if x != '.' else x, list(line))))


# Construct all hiking trails (starting from all trailheads)
print(f'Part 1: {total_score(grid)}')
print(f'Part 2: {total_count(grid)}')

