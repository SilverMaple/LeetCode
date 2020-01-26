#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n==0 else n//5 + self.trailingZeroes(n//5)
# @lc code=end

