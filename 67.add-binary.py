#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ret = []
        while carry==1 or i>=0 or j>=0:
            if i>=0 and a[i] == '1':
                carry += 1
            if j>=0 and b[j] == '1':
                carry += 1
            i -= 1
            j -= 1
            ret.append(carry % 2)
            carry //= 2
        return ''.join([str(i) for i in ret[::-1]]) if ret else '0'

print(Solution().addBinary('11', '1'))
# @lc code=end

