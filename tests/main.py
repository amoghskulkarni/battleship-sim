import unittest

from .invalid_input import InvalidInputUnitTests
from .player_methods import PlayerMethodsUnitTests

def suite():
    suite = unittest.TestSuite()
    
    # Unit tests where the input is invalid
    suite.addTest(InvalidInputUnitTests('test_battleground_size_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_battleground_size_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_too_many'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_invalid_format'))

    # Player class unit tests
    suite.addTest(PlayerMethodsUnitTests('test_moves_setter'))
    suite.addTest(PlayerMethodsUnitTests('test_overdraft_moves'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())