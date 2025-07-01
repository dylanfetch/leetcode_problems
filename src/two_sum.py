from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, value in enumerate(nums):
            if value not in hash_table:
                hash_table[value] = index

        for index, value in enumerate(nums):
            difference = target - value
            if difference in hash_table and hash_table[difference] != index:
                return [index, hash_table[difference]]
            
        return False