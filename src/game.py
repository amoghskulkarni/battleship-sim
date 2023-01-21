"""This file contains the game class for a 2-player game of Battleship.
"""


import logging
from typing import List, Tuple

class Game():
    def __init__(self) -> None:
        self.__n_ships = None
        self.__p1_board = None
        self.__p2_board = None
        self.__p1_ships_destroyed = 0
        self.__p2_ships_destroyed = 0
    
    def set_n_ships(self, n_ships:int) -> None:
        self.__n_ships = n_ships

    def setup_boards(self, n_ships:int, p1_ships:List[Tuple[int, int]], p2_ships:List[Tuple[int, int]]) -> None:
        if not self.__n_ships:
            self.__n_ships = n_ships
        
        # Initialize the player boards
        self.__p1_board = [['-'] * self.__n_ships] * self.__n_ships
        for (ship_loc_x, ship_loc_y) in p1_ships:
            self.__p1_board[ship_loc_x][ship_loc_y] = 'B'
        self.__p2_board = [['-'] * self.__n_ships] * self.__n_ships
        for (ship_loc_x, ship_loc_y) in p2_ships:
            self.__p2_board[ship_loc_x][ship_loc_y] = 'B' 
    
    def register_player_move(self, player_id:int, hit_loc:Tuple[int, int]) -> None:
        (hit_loc_x, hit_loc_y) = hit_loc
        if player_id == 1:
            logging.debug("Player 1 hit a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
            if self.__p2_board[hit_loc_x][hit_loc_y] == 'B':
                self.__p2_board[hit_loc_x][hit_loc_y] = 'X'
                self.__p2_ships_destroyed += 1
            elif self.__p2_board[hit_loc_x][hit_loc_y] == '-':
                self.__p2_board[hit_loc_x][hit_loc_y] = 'O'
        elif player_id == 2:
            logging.debug("Player 2 hit a missile at ({x},{y})".format(x=hit_loc_x, y=hit_loc_y))
            if self.__p1_board[hit_loc_x][hit_loc_y] == 'B':
                self.__p1_board[hit_loc_x][hit_loc_y] = 'X'
                self.__p1_ships_destroyed += 1
            elif self.__p1_board[hit_loc_x][hit_loc_y] == '-':
                self.__p1_board[hit_loc_x][hit_loc_y] = 'O'
        else:
            raise ValueError("Player ID needs to be either 1 or 2.")

    def get_player_scores(self, player_id:int) -> int:
        score = None
        if player_id == 1:
            score = self.__p2_ships_destroyed
        elif player_id == 2:
            score = self.__p1_ships_destroyed
        else:
            raise ValueError("Player ID needs to be either 1 or 2.")
        logging.debug("Player {id} score: {score}".format(id=player_id, score=score))
        return score

    def get_game_result(self) -> str:
        if self.__p1_ships_destroyed == self.__p2_ships_destroyed:
            return "It is a draw"
        elif self.__p1_ships_destroyed > self.__p2_ships_destroyed:
            return "Player 2 wins"
        elif self.__p1_ships_destroyed < self.__p2_ships_destroyed:
            return "Player 1 wins"