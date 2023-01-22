"""This file contains the player class for a 2-player game of Battleship.
"""


from typing import List, Tuple

class Player():
    def __init__(self) -> None:
        """Class containing player moves and a method to return the next move
        """
        self.__moves_list = None
    
    def set_moves_list(self, moves:List[Tuple[int, int]]) -> None:
        """Sets the move list (ideally from the input file) for the player

        Args:
            moves (List[Tuple[int, int]]): List of moves which correspond to the locations of board (i.e. integer tuples)
        """
        # iter object contains the logic of returning the 'next' item in the list 
        # (depending on how many are returned so far), so that we don't have to maintain
        # the index of the item to be returned.
        self.__moves_list = iter(moves)

    def next_move(self) -> Tuple[int, int]:
        """Returns the next move of the player when called.

        Returns:
            Tuple[int, int]: Next move of the player which is a location on the board (i.e. integer tuple)
        """
        # Raises StopIteration error if called more than the number of items 
        return next(self.__moves_list)