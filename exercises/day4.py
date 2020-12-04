#!/usr/bin/env python3
import sys
import re


def password_processing(passports):
  """ Counts the number of valid passports / np credentials from a list of passpors and returns a tuple of the number of valid passports/credentials"""
  pp_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
  npc_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
  n_valid_passports = 0
  n_valid_north_polar_credentials = 0
  
  for passport in passports:
    if all (key in passport for key in pp_keys):
      n_valid_passports += 1
    elif all (key in passport for key in npc_keys):
      n_valid_north_polar_credentials += 1
    else:
      continue
    
  return (n_valid_passports, n_valid_north_polar_credentials)


def password_processing_strict(passports):
  """Counts the amount of valid passports by a certain criteria"""
  pp_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
  n_valid_passports = 0
  for passport in passports:
    # Check that all keys present and contain valid information
    if all(key in passport for key in pp_keys) and validate_fields(passport):
      n_valid_passports += 1
  
  return n_valid_passports


def validate_fields(passport):
  """Validates each field of the passport"""
  valid_byr = len(passport["byr"]) == 4 and (1920 <= int(passport["byr"]) <= 2002)
  valid_iyr = len(passport["iyr"]) == 4 and (2010 <= int(passport["iyr"]) <= 2020)
  valid_eyr = len(passport["eyr"]) == 4 and (2020 <= int(passport["eyr"]) <= 2030)
  valid_ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
  valid_pid = len(passport["pid"]) == 9 and all(x.isdigit() for x in passport["pid"])
  valid_hcl = passport["hcl"][0] == "#" and all(x.isdigit() or x.islower() for x in passport["hcl"][1:])
  hgt_match = re.match(r"([0-9]+)(cm|in)", passport["hgt"])
  if(hgt_match):
    if(hgt_match.groups()[1] == 'cm'):
      valid_hgt = 150 <= int(hgt_match.groups()[0]) <= 193
    else:
      valid_hgt = 59 <= int(hgt_match.groups()[0]) <= 76
  else:
    valid_hgt = False

  return all([valid_byr, valid_iyr, valid_eyr, valid_ecl, valid_pid, valid_hcl, valid_hgt])
  

def processBatchFileInput(f):
  passports, pp = [], {}  
  for line in f:
    if  line == "\n":
      passports.append(pp)
      pp = {}
    else:
      pp.update(dict([x.split(":") for x in line.split()]))

  passports.append(pp)
  return passports


if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    passports = processBatchFileInput(f)
  
  # Part 1
  valids = password_processing(passports)
  print(f"Part 1: Total amount of valid passports: {valids[0] + valids[1]}")
  # Part 2
  valids_2 = password_processing_strict(passports)
  print(f"Part 2: Total amount of valid passports: {valids_2}")

