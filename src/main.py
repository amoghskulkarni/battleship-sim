"""Main executable for Battleship simulator.
"""

from simulator import Simulator
from player import Player
from game import Game

if __name__ == "__main__":
    p1 = Player()
    p2 = Player()
    g = Game()
    s = Simulator(p1=p1, p2=p2, g=g)
    s.read_input('sample-data-1.txt')