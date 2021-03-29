# Let's create test to check if the code whould be running without any errors

from simple_calc import SimpleCals:
# importing the file and class where we would write our code

# importing unittest to inherit TestCase to create our tests against the code
import unittest

class CalcTest(unittest.TestCase):
    calc = SimpleCals()


    def test_add(self): # naming convention - using test in the name of our
# function will let python interpreter know that this needs to be tested
        2 + 2 = 4 outcome is True