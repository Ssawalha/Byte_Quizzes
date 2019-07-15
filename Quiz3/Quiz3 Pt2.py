#./quiz3.sh

#PART 2

# - Now write a unit test for the FizzBuzzer class using the python unittest
#   module.
# - Test that the following.
#   - when `x = FizzBuzzer()`, `x.number` is 0
#   - when `x = FizzBuzzer()`, `x.next()` returns the string `"1"`
#   - when `x = FizzBuzzer(2)`, `x.next()` returns `"fizz"` and calling `x.next()`
#     a second time returns `"4"`
# - You may write other tests as well. Hint: you should not need a setUp() method.

import os
import unittest
from Quiz3 import FizzBuzzer

class TestBuzz(unittest.TestCase):
    
    def test_initial_position(self):
        x = FizzBuzzer()
        self.assertEqual(x.number, 0, 'At FizzBuzzers initial position x.number = 0') 
        self.assertEqual(x.next(), '1', 'At default position, next method returns str(1)')

    def test_position_2(self):
        x = FizzBuzzer(2)
        self.assertEqual(x.next(), 'fizz', 'at pos. 2 returns "fizz"')
        self.assertEqual(x.next(), '4', 'caling next again will return "4"')

