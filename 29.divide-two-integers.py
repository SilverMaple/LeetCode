#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # result = -1
        # while dividend > 0:
        #     dividend -= divisor
        #     result += 1

        # return result

        sig = (dividend < 0) == (divisor < 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            x = 0
            while dividend >= divisor << (x + 1): x += 1 # 2倍加速运算
            res += 1 << x
            dividend -= divisor << x
        return min(res if sig else -res, 2147483647)

