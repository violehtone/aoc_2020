#!/usr/bin/env python3
import sys


def count_answers(form_answers):
  counts = 0
  
  for answer in form_answers:
    counts += len(answer)
  
  return counts


def find_shared_answers(answer_list):
  shared_answers = []
  
  for answer in answer_list:
    shared_answer = ""
    s_answer = "".join(answer)
    unique_answers = "".join(set("".join(answer)))
    
    for ans in unique_answers:
      ans_count = s_answer.count(ans)
      if ans_count == len(answer):
        shared_answer = "".join([shared_answer, ans])
    
    shared_answers.append(shared_answer)
    
  return shared_answers


def find_unique_answers(answer_list):
  form_answers = []
  
  for answer in answer_list:
    unique_answers = "".join(set("".join(answer)))      
    form_answers.append(unique_answers)
    
  return form_answers


def parse_input(f):
  answer_list = []
  raw_input = f.read().split("\n\n")
    
  for line in raw_input:
    answer = line.split("\n")
    answer_list.append(answer)
      
  return answer_list


if __name__ == "__main__":
  with open(sys.argv[1], "r") as f:
    form_answers = parse_input(f)
    
  # Part 1: Sum of answer counts
  unique_answers = find_unique_answers(form_answers)
  answer_counts = count_answers(unique_answers)
  print(f"answer to part 1: {answer_counts}")

  # Part 2: Sum of shared answer counts
  shared_answers = find_shared_answers(form_answers)
  answer_counts2 = count_answers(shared_answers)
  print(f"answer to part 2: {answer_counts2}")