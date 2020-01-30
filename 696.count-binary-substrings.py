#
# @lc app=leetcode id=696 lang=python
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        preLen, curLen, count = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curLen+=1
            else:
                preLen = curLen
                curLen = 1
            if preLen >= curLen:
                count += 1
        return count
# @lc code=end

