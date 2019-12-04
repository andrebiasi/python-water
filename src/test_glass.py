import pytest
from glass import Glass

def test_shouldRaiseExceptionWhenZeroCapacityGiven():
    capacity = 0
    with pytest.raises(ValueError):
        assert Glass(capacity)

def test_shouldRaiseExceptionWhenNegativeCapacityGiven():
    capacity = -1
    with pytest.raises(ValueError):
        assert Glass(capacity)

def test_shouldCreateGlassWhenValidQuantityGiven():
    capacity = 0.25
    glass = Glass(capacity)
    assert glass.capacity == capacity

def test_shouldRaiseExceptionWhenFillingGlassWithNegativeQuantity():
    capacity = 0.25
    quantity = -1
    glass = Glass(capacity)
    with pytest.raises(ValueError):
        assert glass.fill(quantity)

def test_shouldRaiseExceptionWhenFillingGlassWithZeroQuantity():
    capacity = 0.25
    quantity = 0
    glass = Glass(capacity)
    with pytest.raises(ValueError):
        assert glass.fill(quantity)

def test_shouldRaiseExceptionWhenFillingGlassBeyondCapacity():
    capacity = 0.25
    quantity = 0.26
    glass = Glass(capacity)
    with pytest.raises(ValueError):
        assert glass.fill(quantity)

def test_shouldFillGlassWithGivenQuantity():
    capacity = 0.25
    quantity = 0.1
    glass = Glass(capacity)
    glass.fill(quantity)
    assert glass.volume == quantity
    
def test_shouldFillGlassWithFullAmount():
    capacity = 0.25
    quantity = 0.25
    glass = Glass(capacity)
    glass.fill(quantity)
    assert glass.volume == quantity