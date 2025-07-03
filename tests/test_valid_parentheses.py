from src.valid_parentheses import Solution

def test_valid_parentheses_1():
    assert Solution().isValid(s = "()") is True

def test_valid_parentheses_2():
    assert Solution().isValid(s = "()[]{}") is True

def test_valid_parentheses_3():
    assert Solution().isValid(s = "([])") is True

def test_invalid_parentheses_1():
    assert Solution().isValid(s = "(]") is False

def test_invalid_parentheses_1():
    assert Solution().isValid(s = "[") is False

def test_invalid_parentheses_1():
    assert Solution().isValid(s = "]") is False