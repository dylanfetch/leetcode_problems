import pytest
from src.valid_palindrome import Solution

@pytest.mark.parametrize(
        "string, expected",
        [
            ("A man, a plan, a canal: Panama", True),
            (" ", True),
            ("race a car", False)
        ]
)

def test_valid_palindrome(string, expected):
    assert Solution().isPalindrome(s = string) is expected