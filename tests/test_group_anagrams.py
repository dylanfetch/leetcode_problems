import pytest
from src.group_anagrams import Solution

def sort_list_of_lists(list_of_lists):
    return sorted(sorted(inner) for inner in list_of_lists)

@pytest.mark.parametrize(
        "strs, expected",
        [
            (["act","pots","tops","cat","stop","hat"], [["hat"],["act", "cat"],["stop", "pots", "tops"]]),
            (["x"], [["x"]]),
            ([""], [[""]]),
            (["ddddddddddg","dgggggggggg"], [["dgggggggggg"],["ddddddddddg"]])
        ]
)

def test_group_anagrams(strs, expected):
    result = Solution().groupAnagrams(strs = strs)
    assert sort_list_of_lists(result) == sort_list_of_lists(expected)