from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        i = 0
        for num in nums[:-1]:
            prefix.append(prefix[i] * num)
            i += 1

        suffix = [1]
        j = 0
        for num in nums[-1:0:-1]:
            suffix.append(suffix[j] * num)
            j += 1

        output = []
        for pref, suf in zip(prefix, suffix[::-1]):
            output.append(pref * suf)

        return output