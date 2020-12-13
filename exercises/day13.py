#!/usr/bin/env python3
import sys


def create_time_table(earliest_depart_time, busIDs):
  timetable = {}
  for busId in busIDs:
    depart_times = []
    for i in range(0, earliest_depart_time + max(busIDs), busId):
      if(i < earliest_depart_time):
        continue
      else:
        depart_times.append(i)
    timetable[busId] = depart_times
  
  return timetable


def find_earliest_bus(timetable, earliest_depart_time):
  closest_depart_time = max(max(timetable.values()))
  best_bus = 0
  
  for busId, depart_times in timetable.items():
    best_depart_time = min(depart_times, key = lambda x:abs(x-earliest_depart_time))    
    if(best_depart_time < closest_depart_time):
      closest_depart_time = best_depart_time
      best_bus = busId
  
  return (best_bus, closest_depart_time)


def part1(earliest_depart_time, busIDs):
  timetable = create_time_table(earliest_depart_time, busIDs)
  earliest_bus = find_earliest_bus(timetable, earliest_depart_time)
  answer_part1 = earliest_bus[0] * (earliest_bus[1] - earliest_depart_time)
  return answer_part1


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
      lines = f.readlines()
      earliest_depart_time = int(lines[0].strip())
      busIDs = sorted(list(map(int, filter(None, lines[1].replace("x", "").split(",")))))
      
      # Part 1
      ans1 = part1(earliest_depart_time, busIDs)
      print(ans1)
