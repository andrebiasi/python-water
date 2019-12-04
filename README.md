# python-water
python-water is a cli tool to calculate and illustrate how much liquid is in the j’th glass of the i’th row when K litres are poured into the top most glass.

## Pre-requisites
Python 3.x
Pytest

### Running tests
Before running tests, make sure Pytest is installed.
`pip install -U pytest`

To run the tests, execute the command:
`pytest`

### Running the cli tool
`python3 ./src/water_flow.py <row> <column> <amount-of-water-in-litres>`

### Example
`python3 ./src/water_flow.py 1 1 0.25`

### Output
`The amount in row 1, column 1 is: 0.250000`

### Notes
Row and column number start with 1.
Glass capacity is hard-coded to 250ml (0.25L)