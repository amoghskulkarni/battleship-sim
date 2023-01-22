"""Main executable for Battleship simulator.
"""

from .simulator import Simulator
from .player import Player
from .game import Game

import argparse
import logging

# Command line argument parser
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
parser.add_argument(
    '-i', '--input',
    help="Simulation input file name",
    dest="filename",
    default="sample-data-1.txt",
)
args = parser.parse_args()

# Logging level as mentioned in the command-line arguments 
# (Can be set to --debug for the verbose debug messages)
logging.basicConfig(level=args.loglevel)

if __name__ == "__main__":
    # Create a Simulator class object and pass it two Player objects and a Game object 
    s = Simulator(p1=Player(), p2=Player(), g=Game())
    
    # Read input from a file (if not given a command-line argument, defaults to sampel-data-1.txt)
    s.read_input(args.filename)

    # Simulate using the data given in the file
    s.simulate()

    # Writes the result of the simulation in the currospondingly named file in out/
    s.write_result()