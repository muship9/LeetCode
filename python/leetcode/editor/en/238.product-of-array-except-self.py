#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 結果を格納する配列
        res = [1] * len(nums)

        # 左側の積を計算して res に格納
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        # 右側の積を計算しながら res を更新
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# @lc code=end


s = Solution()
print(s.productExceptSelf([1,2,3,4]))