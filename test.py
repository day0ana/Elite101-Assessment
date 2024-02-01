# imports
import unittest
import theaterSeats as t
from main import find_available_seats

class TestSeatFinder(unittest.TestCase):

    def test_find_available_seats(self): # find_available_seats function
        test = find_available_seats(t.theater_seats2)
        self.assertEqual(test, [('1D'),('1E'),('2B'),('2D'),('2F'), ('4B'),('4C'),('5C'),('5F'),('6A'),('6B'),('6C'),('6D'),('6E')])

# planning on adding more soon!

if __name__ == "__main__":
    unittest.main()