# Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  👍 19481 👎 955
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_set = set(nums)
        if len(hash_set) == 1:
            return 1
        else:
            length = 0
            for _, n in enumerate(nums):
                left = n - 1
                right = n + 1
                if left in hash_set or right not in hash_set:
                    continue
                if right in hash_set:
                    count = 1
                    for i in range(len(nums)):
                        target_num = n + 1 * (i + 1)
                        if target_num in hash_set:
                            count = count + 1
                            continue
                        else:
                            if count > length:
                                length = count
                            break
            if length == 0:
                return 1
            else:
                return length

    def longestConsecutive2(self, nums: List[int]) -> int:
        ans = 0
        seen = set(nums)

        for num in nums:
            # 左隣の数値が存在すれば、先頭の要素ではないためスキップ
            if num - 1 in seen:
                continue
            length = 0
            # num が含まれている場合、インクリメントした結果が配列に存在しなくなるまでチェックを行う。
            while num in seen:
                num += 1
                length += 1
            ans = max(ans, length)

        return ans


print(Solution().longestConsecutive2([0]))
print(Solution().longestConsecutive2([0, 0]))
print(Solution().longestConsecutive2([-6, -1, -1, 9, -8, -6, -6, 4, 4, -3, -8, -1]))
print(Solution().longestConsecutive2([-1, 1, 0]))
print(Solution().longestConsecutive2([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(Solution().longestConsecutive2([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))

# leetcode submit region end(Prohibit modification and deletion)
