import pytest
from simple_math import SimpleMath

@pytest.fixture
def math():
    return SimpleMath()

def test_square(math):
    actual_result = math.square(2)
    expected_result = 4
    assert actual_result == expected_result

def test_cube(math):
    actual_result = math.cube(-3)
    expected_result = -27
    assert actual_result == expected_result
