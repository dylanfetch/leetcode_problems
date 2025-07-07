import pytest
from src.contains_duplicate import Solution

@pytest.mark.parametrize(
        "int_list, expected",
        [
            ([1,2,3,4], False),
            ([1,2,3,3], True)
        ]
)

def test_contains_duplicate(int_list, expected):
    assert Solution().hasDuplicate(int_list) is expected