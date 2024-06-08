# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).
#  
# 
#  Find two lines that together with the x-axis form a container, such that the 
# container contains the most water. 
# 
#  Return the maximum amount of water a container can store. 
# 
#  Notice that you may not slant the container. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can 
# contain is 49.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [1,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  2 <= n <= 10⁵ 
#  0 <= height[i] <= 10⁴ 
#  
# 
#  👍 28785 👎 1734
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        output = 0

        left, right = 0, len(height) - 1
        x = 0

        while left < right:
            if height[left] > height[right]:
                x = height[right] * (right - left)
                right -= 1

            elif height[left] < height[right]:
                x = height[left] * (right - left)
                left += 1

            elif height[left] == height[right]:
                x = height[left] * (right - left)
                right -= 1

            if output < x:
                output = x

        return output


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(a.maxArea([1, 1]))
# print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# leetcode submit region end(Prohibit modification and deletion)
