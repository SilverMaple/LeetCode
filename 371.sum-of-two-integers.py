#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return a if b==0 else self.getSum((a^b), (a&b)<<1)
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b!=0:
            a, b = (a^b)&mask, ((a&b)<<1)&mask
        return a if a <= MAX else ~(a^mask)
# @lc code=end

