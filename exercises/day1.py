#!/usr/bin/env python3
import sys


def fixExpenseReport(entries):
  '''Finds 2 numbers (a,b) that sum to 2020 from a list, and then returns the value of a*b'''
  for i in entries:
    for j in entries:
      if i == j:
        continue
      elif i + j == 2020:
        print(f"{i} and {j} sum to 2020")
        return i*j
  # If none matches, return 0
  return 0


def fixExpenseReportPartTwo(entries):
  '''Finds 3 numbers (a,b,c) that sum to 2020 from a list, and then returns the value of a*b*c'''
  for i in entries:
    for j in entries:
      if i == j:
        continue
      elif i + j >= 2020:
        continue
      for k in entries:
        if j == k:
          continue
        elif i+j+k == 2020:
          print(f"{i}, {j}, and {k} sum to 2020")
          return i*j*k
  # If none matches, return 0
  return 0


if __name__ == "__main__":
  entries = []
  with open(sys.argv[1], "r") as f:
    for entry in f:
      entries.append(int(entry.strip("\n")))
      
  # Part 1
  print(fixExpenseReport(entries))
  
  # Part 2
  print(fixExpenseReportPartTwo(entries))