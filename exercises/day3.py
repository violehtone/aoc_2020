#!/usr/bin/env python3
import sys
from functools import reduce

def traverse_map(toboggan_map, slope):
  """ traverses map from top-left to bottom using the instructions given in slope and returns the number of trees encountered"""
  # Set initial coordinates, number of trees, and slope
  ntrees = 0
  x = y = 0
  dx, dy = slope[0], slope[1]
  
  # Traverse through the map
  for line in toboggan_map:
    # Break if at the end of the map or jump to start of the row if at the end
    if y >= len(toboggan_map):
      break
    elif x >= len(toboggan_map[0]):
      x = 0 + (x - len(toboggan_map[0]))
    
    # Count number of trees encountered
    if toboggan_map[y][x] == "#":
      ntrees += 1
      
    # Increment coordinates
    x += dx
    y += dy
         
  return ntrees


def traverse_map_with_multiple_slopes(slopes, toboggan_map):
  ntrees = []
  for slope in slopes:
    ntrees.append(traverse_map(toboggan_map, slope))
  
  return(reduce(lambda x,y : x*y, ntrees))


if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    toboggan_map = f.read().splitlines()
  
  # Part 1
  slope = (3,1)
  ans1 = traverse_map(toboggan_map, slope)
  print(f"Answer to part 1: {ans1}")
  
  # Part 2
  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  ans2 = traverse_map_with_multiple_slopes(slopes, toboggan_map)
  print(f"Answer to part 2: {ans2}")
