from user.points import adjust_points
import pytest

@pytest.mark.parametrize('current_points, adjustment, result', [
    (0, 5, 5),
    (10, -5, 5),
    (20, 'string', 20)
])
def test_adjust_points(current_points, adjustment, result):
    assert adjust_points(current_points, adjustment) == result