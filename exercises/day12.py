#!/usr/bin/env python3
import sys

current_orientation = "east"

def change_orientation(current_orientation, action, degrees):
  orientation = ""
  
  # Turns for east
  if current_orientation == "E":
    if degrees == 180:
      orientation = "W"
    elif degrees == 90:
      if action == "L":
        orientation = "N"
      elif action == "R":
        orientation = "S"
    elif degrees == 270:
      if action == "L":
        orientation = "S"
      elif action == "R":
        orientation = "N"

  # Turns for west
  elif current_orientation == "W":
    if degrees == 180:
      orientation = "E"
    elif degrees == 90:
      if action == "L":
        orientation = "S"
      elif action == "R":
        orientation = "N"
    elif degrees == 270:
      if action == "L":
        orientation = "N"
      elif action == "R":
        orientation = "S"
  
  # Turns for north
  elif current_orientation == "N":
    if degrees == 180:
      orientation = "S"
    elif degrees == 90:
      if action == "L":
        orientation = "W"
      elif action == "R":
        orientation = "E"
    elif degrees == 270:
      if action == "L":
        orientation = "E"
      elif action == "R":
        orientation = "W"
  
  # Turns for south
  elif current_orientation == "S":
    if degrees == 180:
      orientation = "N"
    elif degrees == 90:
      if action == "L":
        orientation = "E"
      elif action == "R":
        orientation = "W"
    elif degrees == 270:
      if action == "L":
        orientation = "W"
      elif action == "R":
        orientation = "E"
  
  
  return orientation


def read_instructions(navigation_instructions):
  pos = [0,0]  # <-- (west-east, north-south)
  orientation = "E"
  
  for instruction in navigation_instructions:
    action = instruction[0]
    value = instruction[1]
    
    if action == "N":
      # move north
      pos[1] += value
    elif action == "S":
      # move south
      pos[1] -= value
    elif action == "E":
      # move east
      pos[0] += value
    elif action == "W":
      # move west
      pos[0] -= value
    elif action == "L":
      # turn left
      orientation = change_orientation(orientation, action, value)
    elif action == "R":
      # turn right
      orientation = change_orientation(orientation, action, value)
    elif action == "F":
      # move forward
      if orientation == "N":
        pos[1] += value
      elif orientation == "S":
        pos[1] -= value
      elif orientation == "E":
        pos[0] += value
      elif orientation == "W":
        pos[0] -= value 
  
  return pos
    
    
def compute_manhattan_distance(pos):
  return abs(pos[0]) + abs(pos[1])
  
    
if __name__ == "__main__":
  navigation_instructions = []
  with open(sys.argv[1], "r") as f:
    for line in f:
      instruction = [line[0], int(line[1:])]
      navigation_instructions.append(instruction)
  
  pos = read_instructions(navigation_instructions)
  print(pos)
  ans1 = compute_manhattan_distance(pos)
  print(ans1)