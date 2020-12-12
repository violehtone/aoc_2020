#!/usr/bin/env python3
import sys      
      
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
        

if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    bag_rules = parse_input(f)