import pytest
from strings_utils import count_char, is_valid_email


@pytest.mark.parametrize("string, char, expected", [
    ("hello", "l", 2),
    ("world", "z", 0),
    ("", "a", 0)
])
def test_count_char(string, char, expected):
    assert count_char(string, char) == expected
    

@pytest.mark.parametrize("email, expected", [
    ("test@test.com", True),
    ("bad-email", False)
])
def test_is_valid_email(email, expected):
    

    assert is_valid_email(email) == expected





