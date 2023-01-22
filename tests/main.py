import unittest

from .invalid_input import InvalidInputUnitTests
from .player_methods import PlayerMethodsUnitTests
from .game_methods import GameMethodsUnitTests
from .simulator_methods import SimulatorMethodsUnitTests

def suite():
    suite = unittest.TestSuite()
    
    # Unit tests where the input is invalid
    suite.addTest(InvalidInputUnitTests('test_battleground_size_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_battleground_size_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_number_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_range_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_nonnumeric'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_number_violation'))
    suite.addTest(InvalidInputUnitTests('test_ship_locations_invalid_format'))

    # Player class unit tests
    suite.addTest(PlayerMethodsUnitTests('test_moves_setter'))
    suite.addTest(PlayerMethodsUnitTests('test_overdraft_moves'))
    
    # Game class unit tests
    suite.addTest(GameMethodsUnitTests('test_board_setter'))
    suite.addTest(GameMethodsUnitTests('test_register_move_hit'))
    suite.addTest(GameMethodsUnitTests('test_register_move_miss'))
    suite.addTest(GameMethodsUnitTests('test_player_scores'))
    suite.addTest(GameMethodsUnitTests('test_game_result'))

    # Simulator class unit test
    suite.addTest(SimulatorMethodsUnitTests('test_simulating_before_reading_input'))
    suite.addTest(SimulatorMethodsUnitTests('test_simulate_without_error'))
    suite.addTest(SimulatorMethodsUnitTests('test_simulate_and_write_output'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())