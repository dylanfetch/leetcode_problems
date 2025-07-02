from src.top_k_frequent_elements import Solution

def test_one():
    result = Solution().topKFrequent(nums = [1,2,2,3,3,3], k = 2)
    assert sorted(result) == [2,3]

def test_two():
    result = Solution().topKFrequent(nums = [7,7], k = 1)
    assert sorted(result) == [7]

def test_three():
    result = Solution().topKFrequent(nums = [4,4,4,-1,-1,2,2,2,2,7], k = 2)
    assert sorted(result) == [2,4]