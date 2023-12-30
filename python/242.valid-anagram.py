#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = sorted(t)
        s_list = sorted(s)
        i = 0
        if len(t_list) != len(s):
            return False
        for tw, sw in zip(t_list, s_list):
            if tw != sw:
                return False
            i += 1
        if i == len(s_list):
            return True
        
    def isAnagram2(self, s: str, t: str) -> bool:
        sort_t = sorted(t)
        sort_s = sorted(s)
        # 配列同士の比較は順番 / 要素の二つが一致する場合 True になるため、これだけで判別可能
        return sort_t == sort_s

# @lc code=end