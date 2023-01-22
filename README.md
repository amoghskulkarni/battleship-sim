# battleship-sim
A simulator for a 2-player game of Battleship

## System requirements
Python 3 (v3.8.8)

## To run the simulator on sample data
Execute the following command in the parent directory containing the repository 
```
python -m battleship-sim.src.main
```

This runs the simulator with sample data provided in [this file](data/sample-data-1.txt).
This should create a new text file in [`out/`](out/) directory, and it should contain the results of the simulation run. 
This file should be identical to [this file](out/result--sample-data-1.txt) in its contents.


## To run the simulator on user-defined data
1. Create a text file in [`out/`](out/) directory in the following format -
```
<Board size M>
<No. of ships available to each player>
<Player 1 ship locations, separated by ',' and x-y coordinates separated by ':'>
<Player 2 ship locations, separated by ',' and x-y coordinates separated by ':'>
<No. of moves i.e. missiles available to each player>
<Player 1 move locations (in the given order), separated by ':' and x-y coordinates separated by ','>
<Player 2 move locations (in the given order), separated by ':' and x-y coordinates separated by ','>
```
Note: Each input has to be present in a single line, lines should not have empty lines in between them.
Inputs spanning lines are not supported.

Please refer to this [sample file](data/sample-data-1.txt) for example of the input data. 

2. Execute the following command in the parent directory containing the repository
```
python -m battleship-sim.src.main --input=<name of the input file>
``` 

This runs the simulator with the data provided in the user-defined text file.
This should create a new text file of a corresponding name (user-defined name, but appended by `Result__` and the system timestamp) 
in [`out/`](out/) directory. This file should contain the results of the simulation run.


## To run the unit tests on the simulator
Execute the following command to run unit tests on the simulator.
```
python -m battleship-sim.tests.main
```

Expected output of running the unit tests -
```
..................
----------------------------------------------------------------------
Ran 18 tests in 0.004s

OK
```

This also creates a new result file in [`out/`](out/) directory as a part of one of the unit tests.
