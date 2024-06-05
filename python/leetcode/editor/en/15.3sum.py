# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not 
# matter.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  👍 30527 👎 2831
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        # hushMap = set()

        for i, n in enumerate(nums):
            # 降順に並び変えてるので後続は n < x となりパターンに一致することはないため処理を終了させる
            if n > 0:
                break

            # 前回の検索値と今回の検索値が同じである場合、パターンは網羅したためスキップ
            # if i > 0 and n == nums[i - 1]:
            #     continue

            # hushMap を管理するメモリや重複チェック時に発生する計算が増えることでオーバーヘッドが起こる可能性があり速度もそこまで変わらないため不採用。
            # if n in hushMap:
            #     continue

            # 左ポインタの1つ大きい値
            left = i + 1
            # 右ポインタとなり nums の大きい値を示す
            right = len(nums) - 1

            while left < right:
                sum = n + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    output.append([n, nums[left], nums[right]])
                    # hushMap.add(n)
                    # left はルートではない。ペアが見つかってもルートの値で複数ペアが見つかる可能性があるためポインタをずらし探索範囲を狭めていく
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return output


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
print(a.threeSum([0, 1, 1]))
print(a.threeSum([0, 0, 0]))

# leetcode submit region end(Prohibit modification and deletion)
