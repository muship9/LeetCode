# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  👍 31788 👎 508
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        for i, n in enumerate(height):

            left = i
            right = i + 1

            if n == 0:
                continue

            while len(height) > right:
                left_val = n
                right_val = height[right]
                if left_val < right_val:
                    right += 1
                    output = output + (right_val - left_val)
                elif left_val > right_val:
                    right += 1
                    output = output + left_val
                elif left_val == right_val:
                    right += 1
                    output = output + (left_val - right_val)

        return output


a = Solution()
print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# leetcode submit region end(Prohibit modification and deletion)
