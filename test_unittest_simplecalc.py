# Let's create test to check if the code whould be running without any errors

from simple_calc import SimpleCalc
# importing the file and class where we would write our code

# importing unittest to inherit TestCase to create our tests against the code
import unittest


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()  # creating an object of our SimpleCalc() class

    def test_add(self):  # naming convention - using test in the name of our
        # function will let python interpreter know that this needs to be tested
        self.assertEqual(self.calc.add(2, 4), 6)
        # this test is checking if 2 + 2 = 6 that would be true, if true test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # This tests the values as 4 - 2 = 2 to be True, if True the test passes

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # This tests the values as 2 * 2 = 4 to be True

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # This tests the values as 15 / 3 = 5 if True the test will pass


# pytest looks for any file with name including test.*.py

