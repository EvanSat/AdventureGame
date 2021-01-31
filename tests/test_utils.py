from samplecode.utils import add, remove_spaces
import pytest

@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (1, 2, 3),
    (5, 10, 15),
    (-1, 5, 4)
])
def test_add(x, y, result):
    assert add(x, y) == result

@pytest.mark.parametrize('data, result', [
    ('Hello world!', 'Helloworld!'),
    ('John Doe', 'JohnDoe'),
    (' ','')
])
def test_remove_spaces(data, result):
    assert remove_spaces(data) == result