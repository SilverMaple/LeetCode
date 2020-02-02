#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num&(num-1) == 0 and (num & 0b01010101010101010101010101010101) != 0
# @lc code=end

