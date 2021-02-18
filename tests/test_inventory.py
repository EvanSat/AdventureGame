from user.inventory import add_to_inventory
import pytest

@pytest.mark.parametrize('current_inventory, new_item, result', [
    (['one item'], 'two item', ['one item', 'two item']),
    ([], 'Friend Maria', ['Friend Maria']),
    ([1, 'string'], 'new', [1, 'string', 'new'])
])
def test_add_to_inventory(current_inventory, new_item, result):
    # Confirm expected types
    assert isinstance(current_inventory, list) == True
    assert isinstance(new_item, str) == True
    assert isinstance(result, list) == True

    assert add_to_inventory(current_inventory, new_item) == result