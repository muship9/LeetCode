# You are given an array of strings tokens that represents an arithmetic 
# expression in a Reverse Polish Notation. 
# 
#  Evaluate the expression. Return an integer that represents the value of the 
# expression. 
# 
#  Note that: 
# 
#  
#  The valid operators are '+', '-', '*', and '/'. 
#  Each operand may be an integer or another expression. 
#  The division between two integers always truncates toward zero. 
#  There will not be any division by zero. 
#  The input represents a valid arithmetic expression in a reverse polish 
# notation. 
#  The answer and all the intermediate calculations can be represented in a 32-
# bit integer. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#  
# 
#  Example 2: 
# 
#  
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#  
# 
#  Example 3: 
# 
#  
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= tokens.length <= 10⁴ 
#  tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
# range [-200, 200]. 
#  
# 
#  👍 7515 👎 1062
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # eval() は式をパース -> コンパイルしてるので、パフォーマンスがよくなく処理に時間がかかる。
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v == '+' or v == '-' or v == '*' or v == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(eval(f"{int(b)} {v} {int(a)}"))
            else:
                stack.append(int(v))
        return int(stack[0])

    # 冗長だがこちらの方が eval を使わない分若干速度が早い
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) + int(a))
            elif v == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif v == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) * int(a))
            elif v == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) / int(a))
            else:
                stack.append(int(v))
        return int(stack[0])


s = Solution()
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN2(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
# print(s.evalRPN(["4", "13", "5", "/", "+"]))

# leetcode submit region end(Prohibit modification and deletion)
