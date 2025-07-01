from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()
        for num in nums:
            if num in hash_table: return True
            hash_table.add(num)
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasDuplicate([1,2,3,4]))
    print(solution.hasDuplicate([1,2,3,3]))