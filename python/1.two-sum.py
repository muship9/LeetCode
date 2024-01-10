#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

from typing import List

class Solution:
    '''
        自分の考えたやつ、配列番号を返せていないため ×
        enumerate() を使って nums から index を取得できるが、key の index を取得するのに再度 nums に対して検索をかける必要があるため効率的ではなさそうと思った。
        また、↑ で取得できた index を hushMap の key に指定し格納するやり方も考えたが、
        1. 取得時に key の指定ができない
        2. husmMap の特性に反し、そもそも hushMap を使わなくて良さそう？
        と考え、dict 型で実装できそうと思いつくも、効率的なやり方がわからないため Solution をチェック。
    '''
    def twoSum(nums: List[int], target: int) -> List[int]:
        hushMap = set()
        arr = []
        for n in nums:
            key = target - n
            if key in hushMap:
                arr += [n, key]
                return arr
            hushMap.add(n)
        return arr

    def twoSumSolutions(nums: List[int], target: int) -> List[int]:
            numMap = {}
            n = len(nums)
            for i in range(n):
                complement = target - nums[i]
                if complement in numMap:
                    return [numMap[complement], i]
                numMap[nums[i]] = i

            return []  # No solution found
# @lc code=end