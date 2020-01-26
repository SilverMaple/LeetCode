#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # subNum = 1
        # while num > 0:
        #     num -= subNum
        #     subNum += 2
        # return num == 0
        r = num
        while r*r > num:
            r = (r + num//r) // 2
        return r*r == num
# @lc code=end

