#
# @lc app=leetcode id=49 lang=python3

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        length = len(strs)
        for i in range(length):
            sorted_s = tuple(sorted(strs[i]))
            if sorted_s in hash_map:
                hash_map[sorted_s].append(strs[i])
            else:
                hash_map[sorted_s] = [strs[i]]
        return list(hash_map.values())


print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
# @lc code=end
