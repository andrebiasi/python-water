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
        numberOfColumns = row + 1
        assert len(stack.stack[row]) == numberOfColumns

def test_shouldCreateStackWith10Rows():
    numberOfRows = 10
    stack = StackOfGlasses(numberOfRows)
    assert len(stack.stack) == numberOfRows
    for row in range(numberOfRows):
        numberOfColumns = row + 1
        assert len(stack.stack[row]) == numberOfColumns

def test_shouldRaiseExceptionWhenPouringNegativeQuantity():
    numberOfRows = 1
    quantity = -1
    stack = StackOfGlasses(numberOfRows)
    with pytest.raises(ValueError):
        stack.pour(quantity)

def test_shouldRaiseExceptionWhenPouringZeroQuantity():
    numberOfRows = 1
    quantity = 0
    stack = StackOfGlasses(numberOfRows)
    with pytest.raises(ValueError):
        stack.pour(quantity)

def test_shouldFillFirstGlass():
    numberOfRows = 2
    quantity = 0.1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.stack[0][0].volume == quantity

def test_shouldFillTotalCapacityFirstGlassAndOverflowDistributedEqually():
    numberOfRows = 2
    quantity = 0.35
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.stack[0][0].volume == stack.stack[0][0].capacity
    assert stack.stack[1][0].volume == pytest.approx(0.05)
    assert stack.stack[1][1].volume == pytest.approx(0.05)

def test_shouldFillMultipleRows():
    numberOfRows = 5
    quantity = 3
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.stack[0][0].volume == stack.stack[0][0].capacity
    assert stack.stack[1][0].volume == stack.stack[0][0].capacity
    assert stack.stack[1][1].volume == stack.stack[0][0].capacity
    assert stack.stack[2][0].volume == stack.stack[0][0].capacity
    assert stack.stack[2][1].volume == stack.stack[0][0].capacity
    assert stack.stack[2][2].volume == stack.stack[0][0].capacity
    assert stack.stack[3][0].volume == stack.stack[0][0].capacity
    assert stack.stack[3][1].volume == stack.stack[0][0].capacity
    assert stack.stack[3][2].volume == stack.stack[0][0].capacity
    assert stack.stack[3][3].volume == stack.stack[0][0].capacity
    assert stack.stack[4][0].volume == pytest.approx(0.1)
    assert stack.stack[4][1].volume == pytest.approx(0.1)
    assert stack.stack[4][2].volume == pytest.approx(0.1)
    assert stack.stack[4][3].volume == pytest.approx(0.1)
    assert stack.stack[4][4].volume == pytest.approx(0.1)

def test_shouldRaiseExceptionWhenGlassDoesntExist():
    numberOfRows = 1
    stack = StackOfGlasses(numberOfRows)
    with pytest.raises(ValueError):
        assert stack.getAmountAt(2,1)

def test_shouldReturnZeroAmount():
    numberOfRows = 1
    stack = StackOfGlasses(numberOfRows)
    assert stack.getAmountAt(1,1) == 0

def test_shouldReturnAmountInGlassInFirstRow():
    numberOfRows = 1
    quantity = 0.1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.getAmountAt(1,1) == pytest.approx(0.1)

def test_shouldReturnAmountInGlassInSecondRow():
    numberOfRows = 2
    quantity = 0.45
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.getAmountAt(2,1) == pytest.approx(0.1)
    assert stack.getAmountAt(2,2) == pytest.approx(0.1)

def test_shouldReturnAmountInGlassInThirdRow():
    numberOfRows = 3
    quantity = 0.45
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    assert stack.getAmountAt(3,1) == 0
    assert stack.getAmountAt(3,2) == 0
    assert stack.getAmountAt(3,3) == 0

def test_shouldRaiseExceptionWhenNegativeRowGiven():
    numberOfRows = 1
    quantity = 1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    with pytest.raises(ValueError):
        assert stack.getAmountAt(-1,1)

def test_shouldRaiseExceptionWhenZeroRowGiven():
    numberOfRows = 1
    quantity = 1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    with pytest.raises(ValueError):
        assert stack.getAmountAt(0,1)

def test_shouldRaiseExceptionWhenNegativeColumnGiven():
    numberOfRows = 1
    quantity = 1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    with pytest.raises(ValueError):
        assert stack.getAmountAt(1,-1)

def test_shouldRaiseExceptionWhenZeroColumnGiven():
    numberOfRows = 1
    quantity = 1
    stack = StackOfGlasses(numberOfRows)
    stack.pour(quantity)
    with pytest.raises(ValueError):
        assert stack.getAmountAt(1,0)