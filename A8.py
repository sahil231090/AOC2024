# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:54:40 2024

@author: sahil
"""

from itertools import product, combinations


grid = []
with open('Q8.txt') as f:
    for line in f:
        
        line = line[:-1]
        
        grid.append(list(line))


rows = len(grid)
cols = len(grid[0])



unique_antinodes_p1 = set()
unique_antinodes_p2 = set()


# Cache
antennas = {}
for r in range(rows):
    for c in range(cols):
        char = grid[r][c]
        # a letter or digit
        if char.isalnum():  
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((r, c))

for freq, positions in antennas.items():
    for (r1, c1), (r2, c2) in combinations(positions, 2):
        

        dx = r2 - r1
        dy = c2 - c1

        i=0
        while True:
            antinode_1 = (r1 - dx * i , c1 - dy * i )
            if 0 <= antinode_1[0] < rows and 0 <= antinode_1[1] < cols:
                unique_antinodes_p2.add(antinode_1)
                if i==1:
                    unique_antinodes_p1.add(antinode_1)
                
                i += 1
            else:
                break
         
        i=0
        while True:    
            antinode_2 = (r2 + dx * i , c2 + dy * i )
            if 0 <= antinode_2[0] < rows and 0 <= antinode_2[1] < cols:
                unique_antinodes_p2.add(antinode_2)
                if i==1:
                    unique_antinodes_p1.add(antinode_2)
                i+=1
            else:
                break
            


# Return the number of unique antinode positions
print(len(unique_antinodes_p1))
print(len(unique_antinodes_p2))

