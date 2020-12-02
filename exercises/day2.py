#!/usr/bin/env python3

import sys

def countValidPasswords(passwords):
  """ Takes a list  of password policies and passwords (tuples) and outputs a number of valid passwords"""
  nValidPasswords = 0
  for p in passwords:
    policy = p[0]
    pw = p[1] 
    limits = policy.split(" ")[0].split("-")
    letter = policy.split(" ")[1]
    
    # Check if password is valid
    if(int(limits[0]) <= pw.count(letter) <= int(limits[1])):
      nValidPasswords += 1
    else:
      print(f"Password: {pw} does not adhere to policy: {policy}")
  
  return nValidPasswords


def countValidPasswordsPartTwo(passwords):
  """ Takes a list  of password policies and passwords (tuples) and outputs a number of valid passwords"""
  nValidPasswords = 0
  for p in passwords:
    policy = p[0]
    pw = p[1] 
    limits = policy.split(" ")[0].split("-")
    letter = policy.split(" ")[1]
    cond1 = pw[int(limits[0]) - 1] == letter
    cond2 = pw[int(limits[1]) - 1] == letter    
    
    if((cond1 and not cond2) or (cond2 and not cond1)):
      nValidPasswords += 1
    else:
      print(f"Password: {pw} does not adhere to policy: {policy}")
  
  return nValidPasswords


def read_input():
  """ Reads the input txt file """
  passwords = []
  with open(sys.argv[1], "r") as f:
    for line in f:
      passwords.append((line.split(":")[0].strip(), line.split(":")[1].strip()))
  return passwords
  

if __name__ == "__main__":
  passwords = read_input()
  ans_part1 = countValidPasswords(passwords)
  ans_part2 = countValidPasswordsPartTwo(passwords)
  print(f"Correct answer to part one is {ans_part1}, and to part two is {ans_part2}")