class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_letters = {}
            t_letters = {}
            for x,y in zip(s,t):
                if x in s_letters:
                    s_letters[x] += 1
                else:
                    s_letters[x] = 1
                
                if y in t_letters:
                    t_letters[y] += 1
                else:
                    t_letters[y] = 1

            if s_letters == t_letters:
                return True

        return False