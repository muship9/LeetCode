# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time. 
# 
#  Implement the MinStack class: 
# 
#  
#  MinStack() initializes the stack object. 
#  void push(int val) pushes the element val onto the stack. 
#  void pop() removes the element on the top of the stack. 
#  int top() gets the top element of the stack. 
#  int getMin() retrieves the minimum element in the stack. 
#  
# 
#  You must implement a solution with O(1) time complexity for each function. 
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= val <= 2³¹ - 1 
#  Methods pop, top and getMin operations will always be called on non-empty 
# stacks. 
#  At most 3 * 10⁴ calls will be made to push, pop, top, and getMin. 
#  
# 
#  👍 13850 👎 859


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        # s に val を追加
        # ms の先頭と val を比較し、小さい方を追加
        self.s.append(val)
        val = min(val, self.ms[-1] if self.ms else val)
        self.ms.append(val)
        # if len(ms) == 0:
        #     ms.append(val)
        # else:
        #     if ms[-1] > val:
        #         ms.append(val)
        #     else:
        #         ms.append(ms[-1])

    def pop(self) -> None:
        # s / ms 共に先頭を削除
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        # s の先頭を取得
        return self.s[-1]

    def getMin(self) -> int:
        # ms の先頭を取得
        return self.ms[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
