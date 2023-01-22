from ..src.player import Player

import unittest

class PlayerMethodsUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Player()
        return super().setUp()
    
    def test_moves_setter(self):
        input_moves = [(1, 2), (2, 3), (3, 4)]
        self.p.set_moves_list(moves=input_moves)
        moves_stored = []
        for _ in range(3):
            moves_stored.append(self.p.next_move())
        self.assertEqual(moves_stored, input_moves)
    
    def test_overdraft_moves(self):
        input_moves = [(1, 2), (2, 3), (3, 4), (5, 3), (1, 3)]
        self.p.set_moves_list(moves=input_moves)
        with self.assertRaises(StopIteration):
            for _ in range(6):
                self.p.next_move()
