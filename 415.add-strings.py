#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ''
        carry = 0
        num1 = list(num1)
        num2 = list(num2)
        while carry>0 or num1 or num2:
            x = int(num1.pop()) if num1 else 0
            y = int(num2.pop()) if num2 else 0
            ret = str((x+y+carry)%10) + ret
            carry = (x+y+carry)//10
        return ret
# @lc code=end

