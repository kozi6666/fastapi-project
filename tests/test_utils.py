from app.utils import add_two_numbers

def test_add_two_numbers():
    result = add_two_numbers(5,3)
    assert result == 8