#!usr/bin/env python3
import sys


def go_through_instructions(instr_args):
  """instr_args is a list of tuples containing 
  instructions and arguments, i.e. ("jmp", 5)"""
  i_values = []
  i = 0
  accumulator = 0
  
  while i < len(instr_args):
    
    # Check if executing for second time
    if(i in i_values):
      break
    else:
      i_values.append(i)
    
    # Handle the instructions / arguments
    instr_arg = instr_args[i]
    if(instr_arg[0] == "acc"):
      accumulator += instr_arg[1]
      i += 1
    elif(instr_arg[0] == "jmp"):
      i += instr_arg[1]
    else:
      i += 1
    
  return accumulator
      

if __name__ == "__main__":
  instr_args = []
  with open(sys.argv[1], "r") as f:
    for line in f:
      line_split = line.split(" ", 1)
      instr_arg = (line_split[0], int(line_split[1].strip()))
      instr_args.append(instr_arg)
print(f"Accumulator value: {go_through_instructions(instr_args)}")