"""This file contains the simulator class for a 2-player game of Battleship.
"""

from player import Player
from game import Game

from pathlib import Path

class Simulator():
    def __init__(self, p1:Player, p2:Player, g:Game) -> None:
        # Game-specific objects
        self.player_1 = p1
        self.player_2 = p2
        self.game = g

        # Game-specific attributes
        self.missiles = None
        self.gridsize = None
        self.player_ships = []

        # IO files / locations
        _this_dir = Path(__file__).parent.resolve()
        self.input_file_dir = _this_dir / '..' / 'data'
        self.output_file_dir = _this_dir / '..' / 'out'
        self.input_file_name = ""
        self.output_file_name = ""

    def simulate(self) -> None:
        pass

    def game_setup(self) -> None:
        pass

    def player_setup(self) -> None:
        pass

    def read_input(self, filename: str) -> None:
        self.input_file_name = filename
        _input_file_abs_path = self.input_file_dir / self.input_file_name
        
        with open(_input_file_abs_path, 'r') as f:
            _contents = f.read()
            print(_contents)

            # Sanity check

            # Initiate objects / set attributes

    def write_result(self, filename: str) -> None:
        pass