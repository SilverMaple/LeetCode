#
# @lc app=leetcode id=633 lang=python
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start = 0
        end = int(c ** 0.5)
        while start <= end:
            cur = start*start + end*end
            if cur < c:
                start += 1
            elif cur > c:
                end -= 1
            else:
                return True
        return False
# @lc code=end

