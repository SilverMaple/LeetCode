#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return ''
        n-=1
        return self.convertToTitle(n//26) + chr(n%26 + ord('A'))

print(Solution().convertToTitle(27))
# @lc code=end

