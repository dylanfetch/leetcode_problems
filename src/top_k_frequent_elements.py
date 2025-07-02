from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        sorted_hash_table_keys = sorted(hash_table, key=hash_table.get, reverse=True)
        

        return sorted_hash_table_keys[:k]
