from ..src.simulator import Simulator
from ..src.game import Game
from ..src.player import Player

import unittest

class InvalidInputUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Simulator(p1=Player(), p2=Player(), g=Game())
        super().setUp()

    def test_battleground_size_range_violation(self):
        with self.assertRaises(ValueError):
            self.s.read_input('unittest--invalid_input1.txt')
    
    def test_battleground_size_nonnumeric(self):
        with self.assertRaises(ValueError):
            self.s.read_input('unittest--invalid_input2.txt')
    
    def test_ship_number_range_violation(self):
        with self.assertRaises(ValueError):
            self.s.read_input('unittest--invalid_input3.txt')
    
    def test_ship_number_nonnumeric(self):
        with self.assertRaises(ValueError):
            self.s.read_input('unittest--invalid_input4.txt')
