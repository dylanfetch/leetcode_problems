from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_dicts = []
        for string in strs:
            hash_table = defaultdict(int)
            for char in string:
                hash_table[char] += 1
            list_of_dicts.append((hash_table,string))

        dict_of_dicts = defaultdict(list)
        for hash_table,string in list_of_dicts:
            dict_of_dicts[frozenset(hash_table.items())].append(string)

        return list(dict_of_dicts.values())