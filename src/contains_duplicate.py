from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                return True
            
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.hasDuplicate([1,2,3,4]))
    print(solution.hasDuplicate([1,2,3,3]))