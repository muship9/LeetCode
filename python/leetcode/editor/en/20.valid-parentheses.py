# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  👍 23595 👎 1688


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        str_list = list(s)
        stack = []
        for sl in str_list:
            if sl in ['(', '[', '{']:
                stack.append(sl)
            else:
                if len(stack) == 0:
                    return False
                sp = stack.pop()
                if not ((sp == '(' and sl == ')') or (sp == '[' and sl == ']') or (sp == '{' and sl == '}')):
                    return False

        return True if len(stack) == 0 else False


s = Solution()

print(s.isValid(s="()"))
print(s.isValid(s="()[]{}"))
print(s.isValid(s="(]"))
# leetcode submit region end(Prohibit modification and deletion)
