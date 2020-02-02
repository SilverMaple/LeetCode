#
# @lc app=leetcode id=476 lang=python
#
# [476] Number Complement
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        mask = 1<<30
        while num&mask == 0:
            mask >>= 1
        mask = (mask<<1) - 1
        return num ^ mask
# @lc code=end

