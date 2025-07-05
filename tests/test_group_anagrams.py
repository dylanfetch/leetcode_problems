from src.group_anagrams import Solution

def sort_list_of_lists(list_of_lists):
    return sorted(sorted(inner) for inner in list_of_lists)

def test_group_anagrams_1():
    result = Solution().groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"])
    expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    assert sort_list_of_lists(result) == sort_list_of_lists(expected)

def test_group_anagrams_2():
    result = Solution().groupAnagrams(strs = ["x"])
    expected = [["x"]]
    assert sort_list_of_lists(result) == sort_list_of_lists(expected)

def test_group_anagrams_3():
    result = Solution().groupAnagrams(strs = [""])
    expected = [[""]]
    assert sort_list_of_lists(result) == sort_list_of_lists(expected)

def test_group_anagrams_4():
    result = Solution().groupAnagrams(["ddddddddddg","dgggggggggg"])
    expected = [["dgggggggggg"],["ddddddddddg"]]
    assert sort_list_of_lists(result) == sort_list_of_lists(expected)