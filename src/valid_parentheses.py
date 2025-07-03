class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_closing_pairs = {"(":")","{":"}","[":"]"}
        for char in s:
            if char in opening_closing_pairs:
                stack.append(char)
            else:
                if len(stack) > 0:
                    last_opening = stack.pop()
                    if char != opening_closing_pairs[last_opening]:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False