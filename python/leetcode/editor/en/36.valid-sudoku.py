# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules: 
# 
#  
#  Each row must contain the digits 1-9 without repetition. 
#  Each column must contain the digits 1-9 without repetition. 
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
# without repetition. 
#  
# 
#  Note: 
# 
#  
#  A Sudoku board (partially filled) could be valid but is not necessarily 
# solvable. 
#  Only the filled cells need to be validated according to the mentioned rules. 
# 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner 
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is 
# invalid.
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit 1-9 or '.'. 
#  
# 
#  Related Topics Array Hash Table Matrix 👍 10402 👎 1095
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_hash = collections.defaultdict(set)  # 横軸
        y_hash = collections.defaultdict(set)  # 縦軸
        square = collections.defaultdict(set)  # 3x3

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if ((board[x][y] in x_hash[x]) or
                        (board[x][y] in y_hash[y]) or
                        (board[x][y] in square[(x // 3, y // 3)])):
                    return False
                x_hash[x].add(board[x][y])
                y_hash[y].add(board[x][y])
                square[(x // 3, y // 3)].add(board[x][y])
        return True
# leetcode submit region end(Prohibit modification and deletion)
