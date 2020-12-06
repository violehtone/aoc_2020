import unittest
import sys
from day6 import parse_input, find_unique_answers, find_shared_answers, count_answers

#* Run the test from command line by:
#* > python -m unittest exercises/test_day6.py

class TestDay6(unittest.TestCase):
  def test_parse_input(self):
    with open("../input_files/day6_test_input.txt", "r") as f:
      parsed_input = parse_input(f)
    self.assertEqual(parsed_input, [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]])  

    
  def test_find_unique_answers(self):
    with open("../input_files/day6_test_input.txt", "r") as f:
      form_answers = parse_input(f)
      unique_answers = find_unique_answers(form_answers)
      answer_counts = count_answers(unique_answers)
      self.assertEqual(answer_counts, 11)
  
  
  def test_find_shared_answers(self):
    with open("../input_files/day6_test_input.txt", "r") as f:
      form_answers = parse_input(f)
      shared_answers = find_shared_answers(form_answers)
      answer_counts = count_answers(shared_answers)
      self.assertEqual(answer_counts, 6)


if __name__ == "__main__":
    unittest.main()