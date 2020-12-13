#!/usr/bin/env python3
import sys      
from copy import deepcopy

def find_more_bags(bag_rules, valid_bag_rules):
  valid_colors = [bag['color'] for bag in valid_bag_rules]

  for bag_rule in bag_rules:
    if not bag_rule['contained_bags']:
      continue
    if any(color in list(bag_rule['contained_bags'].keys()) for color in valid_colors):
      current_colors = [item['color'] for item in valid_bag_rules]
      if bag_rule['color'] not in current_colors:
        valid_bag_rules.append(bag_rule)
  
  return valid_bag_rules
      
      
def find_initial_bags(bag_rules):
  valid_bag_rules = []
  for bag_rule in bag_rules:
    if 'shiny gold' in bag_rule['contained_bags']:
      valid_bag_rules.append(bag_rule)
  return valid_bag_rules


      
def parse_input(f):
  """ Parse the bag rules and returns a list of bag rules"""
  bag_rules = []
  
  for line in f:
    # color
    color = " ".join(line.split(" ")[:2])
    contained_bags_str = " ".join(line.split(" ")[4:]).strip(".,\n")
    contained_bags = {}

    # Handle bags that contain 1 other bga
    if(contained_bags_str.count("bag") == 1 and contained_bags_str != 'no other bags'):
      bag = " ".join(contained_bags_str.split(" ")[1:3])
      amount = int(contained_bags_str[0])
      contained_bags[bag] = amount
      
    # Handle bags that contain multiple bags
    elif(contained_bags_str.count("bag") > 1):
      contained_bags_list = contained_bags_str.split(", ")
      for contained_bag in contained_bags_list:
        bag = " ".join(contained_bag.split(" ")[1:3])
        amount = int(contained_bag[0])
        contained_bags[bag] = amount

    # Append the bag rules list with a new bag object
    bag_rule = {"color" : color, "contained_bags" : contained_bags}
    bag_rules.append(bag_rule)
  
  return bag_rules
        

def part1(bag_rules):
  valid_bags = find_initial_bags(bag_rules)
  answer_p1 = 0
  while(True):
    valid_bags = find_more_bags(bag_rules, valid_bags)
    if len(valid_bags) > answer_p1:
      answer_p1 = len(valid_bags)
    else:
      return answer_p1
    

if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    bag_rules = parse_input(f)
  
  # Part 1
  ans_part1 = part1(bag_rules)
  print("Answer to part 1:", ans_part1)