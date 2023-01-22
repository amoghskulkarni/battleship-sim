from ..src.game import Game

import unittest

class GameMethodsUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Game()
        input_ship_n = 5
        input_ship_loc_p1 = [(1, 2), (2, 4), (2, 3), (3, 4), (4, 0)]
        input_ship_loc_p2 = [(0, 3), (1, 0), (3, 1), (2, 4), (0, 4)]
        self.g.setup_boards(n_ships=input_ship_n, p1_ships=input_ship_loc_p1, p2_ships=input_ship_loc_p2)
        return super().setUp()
    
    def test_board_setter(self):
        board = self.g.get_player_board(player_id=1)
        
        ship_count = sum([line.count('B') for line in board])
        self.assertEquals(ship_count, 5)

        input_ship_loc_p1 = [(1, 2), (2, 4), (2, 3), (3, 4), (4, 0)]
        for s_i in range(5):
            (ship_loc_x, ship_loc_y) = input_ship_loc_p1[s_i]
            self.assertEqual(board[ship_loc_x][ship_loc_y], 'B')
    
    def test_register_move_hit(self):
        board = self.g.get_player_board(player_id=1)

        self.assertEquals(board[1][2], 'B')
        self.g.register_player_move(player_id=2, hit_loc=(1, 2))
        self.assertEquals(board[1][2], 'X')
    
    def test_register_move_miss(self):
        board = self.g.get_player_board(player_id=2)

        self.assertEquals(board[0][3], 'B')
        self.g.register_player_move(player_id=1, hit_loc=(4, 0))
        self.assertEquals(board[0][3], 'B')
        self.assertEquals(board[4][0], 'O')
