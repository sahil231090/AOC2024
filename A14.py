# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:54:02 2024

@author: sahil
"""



def parse_input(filename):
    robots = []
    with open(filename, 'r') as file:
        for line in file:
            p_part, v_part = line.strip().split(' v=')
            p = tuple(map(int, p_part[2:].split(',')))  # Get position (x, y)
            v = tuple(map(int, v_part.split(',')))      # Get velocity (vx, vy)
            robots.append({'p': p, 'v': v})
    return robots

def simulate_robots(robots, time=100):    
    for t in range(time):
        for robot in robots:
            robot['p'] = (
                (robot['p'][0] + robot['v'][0]) % W,  # Wrap around horizontally (width 101)
                (robot['p'][1] + robot['v'][1]) % H   # Wrap around vertically (height 103)
            )

def simulate_robots2(robots):    
    t = 0
    while True:
        # Step 
        for robot in robots:
            robot['p'] = (
                (robot['p'][0] + robot['v'][0]) % W,  # Wrap around horizontally (width 101)
                (robot['p'][1] + robot['v'][1]) % H   # Wrap around vertically (height 103)
            )
        t += 1
        # Check
        if len(robots) == len(set(r['p'] for r in robots)):
            return t


def count_robots_in_quadrants(robots):
    center_x, center_y = int(W/2), int(H/2)
    
    quadrant_counts = [0, 0, 0, 0]
    
    for robot in robots:
        x, y = robot['p']
        
        if x == center_x or y == center_y:
            continue
        
        if x < center_x and y < center_y:
            quadrant_counts[0] += 1  # Top-left
        elif x > center_x and y < center_y:
            quadrant_counts[1] += 1  # Top-right
        elif x < center_x and y > center_y:
            quadrant_counts[2] += 1  # Bottom-left
        elif x > center_x and y > center_y:
            quadrant_counts[3] += 1  # Bottom-right
    
    return quadrant_counts

def safety_factor(quadrant_counts):
    return quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]

    
W = 101
H = 103

filename = "Q14.txt"
robots = parse_input(filename)

## Part 1
simulate_robots(robots, time=100)
quadrant_counts = count_robots_in_quadrants(robots)
factor = safety_factor(quadrant_counts)

print(f"Safety Factor: {factor}")


## Part 2
t = simulate_robots2(robots)
print(f"Time to Unique: {t}")
