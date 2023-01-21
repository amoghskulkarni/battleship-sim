"""This file contains the simulator class for a 2-player game of Battleship.
"""

from player import Player
from game import Game

import logging
from pathlib import Path
from typing import List
from enum import Enum

class SimInputs(Enum):
    BATTLEGROUND_SIZE = 0
    N_SHIPS = 1
    P1_POS_SHIPS = 2
    P2_POS_SHIPS = 3
    N_MISSILES = 4
    P1_MOVES = 5
    P2_MOVES = 6

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
    
    def __numeric_input_sanity_check(self, _raw_input, _input_name, _line_n, _lower, _upper) -> int:
        try:
            __input = int(_raw_input)
        except ValueError:
            raise ValueError("{name} is in invalid format. (Battleship input file: Line {line_n})"
                                .format(name=_input_name, line_n=_line_n))
        except:
            raise
        else:
            if __input <= _lower:
                raise ValueError('{name} must be greater than {bound}. (Battleship input file: Line {line_n})'
                                .format(name=_input_name, bound=_lower, line_n=_line_n))
            if __input >= _upper:
                raise ValueError('{name} must be less than {bound}. (Battleship input file: Line {line_n})'
                                .format(name=_input_name, bound=_upper, line_n=_line_n))
        return __input
    
    def __list_input_sanity_check(self, _raw_input, _input_name, _line_n, _listsep, _item_sep, _list_len, _list_item_lower, _list_item_upper):
        __input_list = []
        try:
            __input_list_split = _raw_input.split(_listsep)
            for __list_item in __input_list_split:
                input = list(map(int, __list_item.split(_item_sep)))
                __input_list.append(input)
        except ValueError:
            raise ValueError("One or more inputs in {name} is in invalid format. (Battleship input file: Line {line})"
                                .format(name=_input_name, line=_line_n))
        except:
            raise
        else:
            if len(__input_list) != _list_len:
                raise ValueError("Number of inputs in {name} must match {list_len}. (Battleship input file: Line {line})"
                                .format(name=_input_name, line=_line_n, list_len=_list_len))
            for [in_x, in_y] in __input_list:
                if in_x <= _list_item_lower or in_x >= _list_item_upper or in_y <= _list_item_lower or in_y >= _list_item_upper:
                    raise ValueError("One or more input item in {name} is not in the range [{lower}, {upper}]. (Battleship input file: Line {line})"
                                .format(name=_input_name, line=_line_n, lower=_list_item_lower, upper=_list_item_upper))
        return __input_list

    def __input_sanity_check(self, _inputs: List) -> None:
        inputs_dict = {}
        for input in SimInputs:
            if input == SimInputs.BATTLEGROUND_SIZE:
                __M_raw = _inputs[input.value]
                logging.debug("M = {}".format(__M_raw))
                inputs_dict['M'] = self.__numeric_input_sanity_check(__M_raw, 'Battleground size input (M)', 1, 0, 10)
            elif input == SimInputs.N_SHIPS:
                __S_raw = _inputs[input.value]
                logging.debug("N = {}".format(__S_raw))
                inputs_dict['S'] = self.__numeric_input_sanity_check(__S_raw, 'Number of ships (S)', 2, 0, int(inputs_dict['M']**2/2))
            elif input == SimInputs.P1_POS_SHIPS:
                __P1_POS_SHIPS_raw = _inputs[input.value]
                logging.debug("P1_POS_SHIPS = {}".format(__P1_POS_SHIPS_raw))
                inputs_dict['P1_SHIP_POS'] = self.__list_input_sanity_check(__P1_POS_SHIPS_raw, 'Player 1 ship positions', 
                                                                                3, ',', ':', inputs_dict['S'], -1, inputs_dict['M'])
            elif input == SimInputs.P2_POS_SHIPS:
                __P2_POS_SHIPS_raw = _inputs[input.value]
                logging.debug("P2_POS_SHIPS = {}".format(__P2_POS_SHIPS_raw))
                inputs_dict['P2_SHIP_POS'] = self.__list_input_sanity_check(__P2_POS_SHIPS_raw, 'Player 2 ship positions', 
                                                                                4, ',', ':', inputs_dict['S'], -1, inputs_dict['M'])
            elif input == SimInputs.N_MISSILES:
                __T_raw = _inputs[input.value]
                logging.debug("T = {}".format(__T_raw))
                inputs_dict['T'] = self.__numeric_input_sanity_check(__T_raw, 'Number of missiles (T)', 5, 0, 100)
            elif input == SimInputs.P1_MOVES:
                __P1_MOVES_raw = _inputs[input.value]
                logging.debug("P1_MOVES = {}".format(__P1_MOVES_raw))
                inputs_dict['P1_MOVES'] = self.__list_input_sanity_check(__P1_MOVES_raw, 'Player 1 moves', 
                                                                                6, ':', ',', inputs_dict['T'], -1, inputs_dict['M'])
            elif input == SimInputs.P2_MOVES:
                __P2_MOVES_raw = _inputs[input.value]
                logging.debug("P2_MOVES = {}".format(__P2_MOVES_raw))
                inputs_dict['P2_MOVES'] = self.__list_input_sanity_check(__P2_MOVES_raw, 'Player 2 moves', 
                                                                                7, ':', ',', inputs_dict['T'], -1, inputs_dict['M'])
        
        logging.debug("Sanitized inputs: {}".format(str(inputs_dict)))
        return inputs_dict
    
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
            _contents = f.read().split('\n')
            
            # Sanity check
            inputs = self.__input_sanity_check(_contents)

            # Initiate objects / set attributes

    def write_result(self, filename: str) -> None:
        pass