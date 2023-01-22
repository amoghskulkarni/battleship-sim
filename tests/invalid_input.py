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

