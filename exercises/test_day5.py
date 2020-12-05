import unittest
from day5 import solve_seat_ID, decode_seat


class TestDay5(unittest.TestCase):  
  
  def test_solve_seat_id(self):
    seat = (44, 5)
    self.assertEqual(solve_seat_ID(seat), 357)
  
  
  def test_decode_seat(self):
    bsps = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    self.assertEqual(decode_seat(bsps[0]), (70,7))
    self.assertEqual(decode_seat(bsps[1]), (14,7))
    self.assertEqual(decode_seat(bsps[2]), (102,4))


if __name__ == "__main__":
    unittest.main()