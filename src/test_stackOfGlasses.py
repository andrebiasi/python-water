import pytest
from stackOfGlasses import StackOfGlasses

def test_shouldRaiseExceptionWhenZeroRowsGiven():
    numberOfRows = 0
    with pytest.raises(ValueError):
        assert StackOfGlasses(numberOfRows)

def test_shouldRaiseExceptionWhenNegativeRowsGiven():
    numberOfRows = -1
    with pytest.raises(ValueError):
        assert StackOfGlasses(numberOfRows)

def test_shouldRaiseExceptionWhenNonIntegerRowsGiven():
    numberOfRows = 1.1
    with pytest.raises(ValueError):
        assert StackOfGlasses(numberOfRows)

def test_shouldCreateStackWith1Row():
    numberOfRows = 1
    stack = StackOfGlasses(numberOfRows)
    assert len(stack.stack) == numberOfRows

def test_shouldCreateStackWith2Rows():
    numberOfRows = 2
    stack = StackOfGlasses(numberOfRows)
    assert len(stack.stack) == numberOfRows
    for row in range(numberOfRows):
        assert len(stack.stack[row]) == row

def test_shouldCreateStackWith10Rows():
    numberOfRows = 10
    stack = StackOfGlasses(numberOfRows)
    assert len(stack.stack) == numberOfRows
    for row in range(numberOfRows):
        assert len(stack.stack[row]) == row