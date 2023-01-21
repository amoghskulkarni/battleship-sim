"""Main executable for Battleship simulator.
"""

from simulator import Simulator
from player import Player
from game import Game

import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug',
    help="Print lots of debugging statements",
    action="store_const", dest="loglevel", const=logging.DEBUG,
    default=logging.WARNING,
)
parser.add_argument(
    '-v', '--verbose',
    help="Be verbose",
    action="store_const", dest="loglevel", const=logging.INFO,
)
args = parser.parse_args()
logging.basicConfig(level=args.loglevel)

if __name__ == "__main__":
    s = Simulator(p1=Player(), p2=Player(), g=Game())
    s.read_input('sample-data-1.txt')
    print(s.get_result())
    