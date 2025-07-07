import pytest
from src.valid_parentheses import Solution

@pytest.mark.parametrize(
        "string, expected",
        [
            ("()", True),
            ("()[]{}", True),
            ("([])", True),
            ("(]", False),
            ("[", False),
            ("]", False)
        ]
)

def test_valid_parentheses(string, expected):
    assert Solution().isValid(s = string) is expected