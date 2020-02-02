#
# @lc app=leetcode id=693 lang=python
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = n ^ (n>>1)
        return a&(a+1) == 0
# @lc code=end

