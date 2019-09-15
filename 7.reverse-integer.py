#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.19%)
# Total Accepted:    629.2K
# Total Submissions: 2.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # neg = x<0
        # s = [c for c in str(-x if neg else x)]
        # s.reverse()
        # s = int(''.join(s))
        # s = -s if neg else s
        # print(s)
        # return s

        # Runtime: 24 ms beats 100%
        # Memory Usage: 10.9 MB
        neg = x < 0
        if neg: rev = int('-' + str(-x)[::-1])
        else: rev = int(str(x)[::-1])
        if rev > 2**31 or rev < -2**31 - 1:
            return 0
        return rev
        
s = Solution()
s.reverse(123456789)
s.reverse(-123456789)

