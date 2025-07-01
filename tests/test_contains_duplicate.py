from src.contains_duplicate import Solution

def test_no_duplicates():
    assert Solution().hasDuplicate([1,2,3,4]) is False

def test_with_duplicates():
    assert Solution().hasDuplicate([1,2,3,3]) is True