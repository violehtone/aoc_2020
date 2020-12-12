#!/usr/bin/env python3
import sys


def find_num_not_sum_of_two(numbers):
  for i in range(0, len(numbers)):
    preamble = numbers[i:i+25]
    next_number = numbers[i+25]
    matches = []
    for n1 in preamble:
      for n2 in preamble:
        if n1 + n2 != next_number:
          matches.append(False)
        else:
          matches.append(True)
    if(True not in matches):
      return next_number
    

def parse_input(f):
  numbers = []
  for line in f:
    numbers.append(int(line))
  return numbers    
  

if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
      numbers = parse_input(f)
  
  # Part 1
  n = find_num_not_sum_of_two(numbers)
  print(n)
  
  # Part 2
  n_sets = find_set_of_numbers_summing_to_n(numbers, n)
  print(n_sets)
  

    