from src.valid_palindrome import Solution

def test_valid_palindrome_1():
    assert Solution().isPalindrome(s = "A man, a plan, a canal: Panama") is True

def test_valid_palindrome_2():
    assert Solution().isPalindrome(s = " ") is True

def test_invalid_palindrome_1():
    assert Solution().isPalindrome(s = "race a car") is False