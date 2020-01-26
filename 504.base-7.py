#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        ret = ''
        negative = num < 0
        num = abs(num)
        while num>0:
            ret = str(num%7) + ret
            num //= 7
        return '-'+ret if negative else ret

# @lc code=end

