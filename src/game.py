"""This file contains the game class for a 2-player game of Battleship.
"""


import logging
from typing import List, Tuple

class Game():
    def __init__(self) -> None:
        """Class containing members and methods for storing and manipulating player battlegrounds
        """
        self.__n_ships = None
        self.__p1_board = None
        self.__p2_board = None
        self.__p1_ships_destroyed = 0
        self.__p2_ships_destroyed = 0
    
    def set_n_ships(self, n_ships:int) -> None:
        """Sets the number of ships that players are allowed to place

        Args:
            n_ships (int): Number of ships
        """
        self.__n_ships = n_ships

    def setup_boards(self, n_ships:int, p1_ships:List[Tuple[int, int]], p2_ships:List[Tuple[int, int]]) -> None:
        """Sets up the battlegrounds ('player boards') in the form of list of lists for simulating the game

        Args:
            n_ships (int): Number of ships the players are allowed to place
            p1_ships (List[Tuple[int, int]]): Locations of the ships of Player 1
            p2_ships (List[Tuple[int, int]]): Locations of the ships of Player 2
        """
        if not self.__n_ships:
            self.__n_ships = n_ships
        
        # Initialize the player boards
        self.__p1_board = [['_'] * self.__n_ships for _ in range(self.__n_ships)]
        for (ship_loc_x, ship_loc_y) in p1_ships:
            self.__p1_board[ship_loc_x][ship_loc_y] = 'B'
        self.__p2_board = [['_'] * self.__n_ships for _ in range(self.__n_ships)]
        for (ship_loc_x, ship_loc_y) in p2_ships:
            self.__p2_board[ship_loc_x][ship_loc_y] = 'B' 
    
    def register_player_move(self, player_id:int, hit_loc:Tuple[int, int]) -> None:
        """Registers player move on the other player's battleground (board)

        Args:
            player_id (int): ID of the player making the move (either 1 or 2).
            hit_loc (Tuple[int, int]): Location where the player is making the move. Either hits or misses.

        Raises:
            ValueError: If the player ID is not 1 or 2. 
        """
        (hit_loc_x, hit_loc_y) = hit_loc
        if player_id == 1:
            if self.__p2_board[hit_loc_x][hit_loc_y] == 'B':
                self.__p2_board[hit_loc_x][hit_loc_y] = 'X'
                logging.debug("Player 1 hit a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
                self.__p2_ships_destroyed += 1
            elif self.__p2_board[hit_loc_x][hit_loc_y] == '_':
                self.__p2_board[hit_loc_x][hit_loc_y] = 'O'
                logging.debug("Player 1 missed a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
        elif player_id == 2:
            if self.__p1_board[hit_loc_x][hit_loc_y] == 'B':
                self.__p1_board[hit_loc_x][hit_loc_y] = 'X'
                logging.debug("Player 2 hit a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
                self.__p1_ships_destroyed += 1
            elif self.__p1_board[hit_loc_x][hit_loc_y] == '_':
                self.__p1_board[hit_loc_x][hit_loc_y] = 'O'
                logging.debug("Player 2 missed a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
        else:
            raise ValueError("Player ID needs to be either 1 or 2.")

    def get_player_scores(self, player_id:int) -> int:
        """Gets the score of a player depending on the current state of the other player's board

        Args:
            player_id (int): ID of the player. (Should be either 1 or 2)

        Raises:
            ValueError: If player ID is other than 1 or 2

        Returns:
            int: Player score
        """
        score = None
        if player_id == 1:
            score = self.__p2_ships_destroyed
        elif player_id == 2:
            score = self.__p1_ships_destroyed
        else:
            raise ValueError("Player ID needs to be either 1 or 2.")
        logging.debug("Player {id} score: {score}".format(id=player_id, score=score))
        return score
    
    def get_player_board(self, player_id:int) -> List[List[str]]:
        """Current state of a player's battleground board

        Args:
            player_id (int): ID of the player (should be either 1 or 2)

        Raises:
            ValueError: If the player ID is other than 1 or 2

        Returns:
            List[Tuple[int, int]]: The board (list of list of chars) where each location is either '_', 'O', 'X' or 'B'
        """
        board = None
        if player_id == 1:
            board = self.__p1_board
        elif player_id == 2:
            board = self.__p2_board
        else:
            raise ValueError("Player ID needs to be either 1 or 2.")
        logging.debug("Player {id} board returned.".format(id=player_id))
        return board

    def get_game_result(self) -> str:
        """Returns the game result by comparing players' scores

        Returns:
            str: Either "It is a draw", "Player 1 wins" or "Player 2 wins" depending on player scores
        """
        game_result = ''
        if self.__p1_ships_destroyed == self.__p2_ships_destroyed:
            game_result = "It is a draw"
        elif self.__p1_ships_destroyed > self.__p2_ships_destroyed:
            game_result = "Player 2 wins"
        elif self.__p1_ships_destroyed < self.__p2_ships_destroyed:
            game_result = "Player 1 wins"
        logging.debug("Game result: {result}".format(result=game_result))
        return game_result