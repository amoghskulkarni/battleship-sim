import unittest

from .invalid_input import InvalidInputUnitTests

def suite():
    suite = unittest.TestSuite()
    suite.addTest(InvalidInputUnitTests('test_battleground_size_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_battleground_size_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_nonnumeric'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())