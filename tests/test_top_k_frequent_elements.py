import pytest
from src.top_k_frequent_elements import Solution

@pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1,2,2,3,3,3], 2, [2,3]),
            ([7,7], 1, [7]),
            ([4,4,4,-1,-1,2,2,2,2,7], 2, [2,4])
        ]
)

def test_top_k_frequent_elements(nums, k, expected):
    result = Solution().topKFrequent(nums = nums, k = k)
    assert sorted(result) == expected