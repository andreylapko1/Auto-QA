import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    return SimpleMath()

@pytest.mark.parametrize('a, b', [
    (2,4),
    (-3,-27),

])



# @pytest.mark.skipif(1 == 1,reason="not implemented")
def test_square(math, a, b):

    actual_result = math.square(a)
    expected_result = b
    assert actual_result == expected_result

def test_cube(math,a,b):
    actual_result = math.cube(a)
    expected_result = b
    assert actual_result == expected_result


