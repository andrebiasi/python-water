# python-water
python-water is a cli tool to calculate and illustrate how much liquid is in the j’th glass of the i’th row when K litres are poured into the top most glass.

## Pre-requisites
Python 3.x
Pytest

### Running tests
Before running tests, make sure Pytest is installed.
`pip install -U pytest`

To run the tests, execute the command below:
`pytest`

### Running the cli tool
`python3 python-water <glass-capacity-in-litres> <row> <column> <amount-of-water-in-litres>`

### Example
`python3 python-water 0.25 2 2 1