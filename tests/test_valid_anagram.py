import pytest
from src.valid_anagram import Solution

@pytest.mark.parametrize(
        "string, target, expected",
        [
            ("anagram", "nagaram", True),
            ("rat", "car", False)
        ]
)
def test_valid_anagram(string, target, expected):
    assert Solution().isAnagram(s = string, t = target) is expected