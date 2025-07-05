import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True

        clean_string = re.sub(r'[^a-zA-Z0-9]', '', s)

        if clean_string.lower() == clean_string[::-1].lower():
            return True
        else:
            return False