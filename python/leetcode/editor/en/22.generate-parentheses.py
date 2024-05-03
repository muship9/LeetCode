# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
# 
#  👍 20766 👎 902
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # 1 < n < 8 となるため、必ずこの条件からスタート
            # openN == closedN == n で n 分の括弧追加完了後 return されることで、呼び出し元で stack 内の () が1つずつ削除される
            # ↑ を削除対象がなくなるまで繰り返す。
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()

        backTrack(0, 0)
        return res


a = Solution()
print(a.generateParenthesis(3))
# leetcode submit region end(Prohibit modification and deletion)
