# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the iᵗʰ day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead. 
# 
#  
#  Example 1: 
#  Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#  
#  Example 2: 
#  Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#  
#  Example 3: 
#  Input: temperatures = [30,60,90]
# Output: [1,1,0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= temperatures.length <= 10⁵ 
#  30 <= temperatures[i] <= 100 
#  
# 
#  👍 12989 👎 311=
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        # res に値を append したら counter を初期化する。
        def backTrack(num, target):
            counter = 0

            if target > len(temperatures):
                res.append(counter)
                counter = 0
                return

            left = temperatures[num]
            right = temperatures[target]

            if left > right:
                res.append(counter)
                counter = 0
                return

            if left < right:
                counter = counter + 1
                backTrack(num, target + 1)

        for i in range(len(temperatures)):
            backTrack(i, i + 1)
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
