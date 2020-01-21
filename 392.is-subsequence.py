#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = -1
        for c in s:
            try:
                index = t.index(c, index+1)
            except ValueError:
                return False
        return True
# @lc code=end

