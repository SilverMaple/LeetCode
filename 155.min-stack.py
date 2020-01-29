#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.dataStack.append(x)
        self.min = min(self.min, x)
        self.minStack.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        self.dataStack.pop()
        self.minStack.pop()
        self.min = float('inf') if not self.minStack else self.minStack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.dataStack[-1] if self.dataStack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1] if self.minStack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

