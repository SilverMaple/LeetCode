#
# @lc app=leetcode id=405 lang=python
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        symb = 'abcdef'
        num &= 0xFFFFFFFF
        res = []
        while num:
            cur = num % 16
            res.append(str(cur) if cur < 10 else symb[cur-10])
            num //= 16
        return ''.join(res[::-1]) if res else '0'

print(Solution().toHex(-1))
# @lc code=end

