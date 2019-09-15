#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        res = 0

        for i in range(len(s)-1):
            if roman_map[s[i]]< roman_map[s[i+1]]:
                res = res - roman_map[s[i]]
            else:
                res = res + roman_map[s[i]]

        return res + roman_map[s[-1]]

