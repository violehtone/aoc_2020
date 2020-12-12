#!/usr/bin/env python3
import sys

def get_device_adapter_rate(output_joltages):
  return max(output_joltages) + 3
  

def parse_input(f):
  output_joltages = []
  for line in f:
    output_joltages.append(int(line))
  return output_joltages    


def part1(f):
  # Set charging outlet effective rating
  charging_outlet = 0
  
  # Get the output joltages of joltage adapters
  adapter_output_joltages = parse_input(f)
  
  # Get device adapter rate
  device_adapter_rate = get_device_adapter_rate(adapter_output_joltages)
  
  # Add device adapter- and charging outlet rates
  adapter_output_joltages.append(charging_outlet)
  adapter_output_joltages.append(device_adapter_rate)
  
  # Sort the output joltages
  adapter_output_joltages.sort()
  
  # Get differences between the joltages
  joltage_differences = [j-i for i, j in zip(adapter_output_joltages[:-1], adapter_output_joltages[1:])]
  
  # Get device adapter rate
  device_adapter_rate = get_device_adapter_rate(adapter_output_joltages)
  
  return joltage_differences.count(1) * joltage_differences.count(3)

    
if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    ans1 = part1(f)
    print(f"answer to part 1: {ans1}")
    
  

  

    