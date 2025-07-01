from src.two_sum import Solution

def test_one():
    result = Solution().twoSum(nums = [2,7,11,15], target = 9)
    assert sorted(result) == [0,1]

def test_two():
    result = Solution().twoSum(nums = [3,2,4], target = 6)
    assert sorted(result) == [1,2]

def test_three():
    result = Solution().twoSum(nums = [3,3], target = 6)
    assert sorted(result) == [0,1]