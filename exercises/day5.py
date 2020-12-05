#!/usr/bin/env python3
import sys


def find_your_seat_id(seats):
  seat_IDs = []
  for seat in seats:
    seat_IDs.append(solve_seat_ID(seat))
    seat_IDs = sorted(seat_IDs)

  my_seat_ID = [x for x in range(seat_IDs[0], seat_IDs[-1]+1) if x not in seat_IDs]
  return my_seat_ID[0]


def decode_seats(boarding_passes):
  seats = []
  for boarding_pass in boarding_passes:
    seat = decode_seat(boarding_pass)
    seats.append(seat)
  return seats


def solve_seat_ID(seat):
  """ Takes seat (row, col) as input. Multiplies seat row by 8 and adds the column"""
  return seat[0] * 8 + seat[1]


def find_highest_seat_ID(seats):
  maxID = 0
  for seat in seats:
    seat_id = solve_seat_ID(seat)
    if seat_id > maxID:
      maxID = seat_id
  
  return maxID


def decode_seat(bsp):
  """ decodes the seat (row, col) from a binary space partitioning (bsp)"""
  row = range(0,128)
  col = range(0,8)
  
  # Solve row
  row_codes = bsp[:7]
  for row_code in row_codes:
    if(row_code == "F"):
      row = row[:len(row) // 2]
    elif(row_code == "B"):
      row = row[len(row) // 2:]
    else:
      print("Invalid row code")
      break
      
  # solve column
  col_codes = bsp[7:]
  for col_code in col_codes:
    if(col_code == "L"):
      col = col[:len(col) // 2]
    elif(col_code == "R"):
      col = col[len(col) // 2:]
    else:
      print("Invalid col code")
      break
  
  return (row[0], col[0])


def readBoardingPasses(args):
  with open(args, "r") as f:  
    return f.read().splitlines()
  

if __name__ == "__main__":
  boarding_passes = readBoardingPasses(sys.argv[1])
  seats = decode_seats(boarding_passes)
  highest_ID = find_highest_seat_ID(seats)
  
  # Part1
  print(f"Highest ID found: {highest_ID}")
  
  # Part2
  my_seat_ID = find_your_seat_id(seats)
  print(f"Your seat ID is: ", my_seat_ID)