from ..src.simulator import Simulator
from ..src.game import Game
from ..src.player import Player

import unittest

class SimulatorMethodsUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Simulator(p1=Player(), p2=Player(), g=Game())
        return super().setUp()
    
    def test_simulating_before_reading_input(self):
        with self.assertRaises(RuntimeError):
            self.s.simulate()
    
    def test_simulate_without_error(self):
        self.s.read_input('unittest--input1.txt')
        self.assertEquals(self.s.simulate(), None)
    
    def test_simulate_and_write_output(self):
        self.s.read_input('unittest--input1.txt')
        self.s.simulate()
        self.s.write_result()
