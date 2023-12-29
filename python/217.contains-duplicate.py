#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

class Solution:
    # 6464 ms
    # 自分のコード、タイムアウトが起きてしまう。
    def containsDuplicate(self, nums: List[int]) -> bool:
        r = []
        for n in nums:
            if n in r:
                return True
            r.append(n)
        return False
    
    # 109 ms
    # set() がハッシュテーブルを使って要素の一意性をチェックするため配列より高速である
    def containsDuplicateHush(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# @lc code=end
