# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include letters and numbers.
#
#  Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#  Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
#  Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#  Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 2 * 10⁵
#  s consists only of printable ASCII characters.
#
#
#  👍 9167 👎 8318
import re


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        format_s = re.sub(r'\W|_', '', s.lower())
        left = 0
        right = len(format_s) - 1
        while left < right:
            if format_s[left] != format_s[right]:
                return False
            left = left + 1
            right = right - 1

        return True


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))
print(a.isPalindrome(" "))
print(a.isPalindrome("ab_a"))

# leetcode submit region end(Prohibit modification and deletion)
