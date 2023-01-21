"""This file contains the player class for a 2-player game of Battleship.
"""


from typing import List, Tuple

class Player():
    def __init__(self) -> None:
        self.__moves_list = None
    
    def set_moves_list(self, moves:List[Tuple[int, int]]) -> None:
        self.__moves_list = iter(moves)

    def next_move(self) -> List[Tuple[int, int]]:
        next(self.__moves_list)