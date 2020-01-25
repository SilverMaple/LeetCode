#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        pre2, pre1 = 1, 2
        for i in range(2, n):
            cur = pre1 + pre2
            pre2 = pre1
            pre1 = cur
        return pre1
# @lc code=end

