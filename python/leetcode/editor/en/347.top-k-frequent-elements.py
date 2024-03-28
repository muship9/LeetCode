#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.79%)
# Likes:    16675
# Dislikes: 615
# Total Accepted:    1.9M
# Total Submissions: 3M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # nums 分の配列の長さを持つ
        freq = [[] for n in range(len(nums) + 1)]

        # ここで count に n をキーとする出現回数を定義、初期値は 0 となる
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # count に格納した出現回数を配列分の長さを持つ freq の自身の番号に出現回数を格納
        for n, c in count.items():
            freq[c].append(n)

        # 配列数分のループ処理を行い、指定の数値のみ res に追加する
        # range(len(freq) -1, 0, -1): は配列の長さ分の int を昇順で行う( 例 配列の長さ = 4 であれば 4,3,2,1 の順でループが行われる)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if(len(res) == k):
                return res



        
a = Solution()
# print(a.topKFrequent([3, 3, 1, 1, 2, 1, 3, 1, 2], 2))
print(a.topKFrequent([3, 3, 1, 1, 2, 1, 3, 1, 2], 2))

# @lc code=end

