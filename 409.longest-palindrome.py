#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = sum(v&1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
# @lc code=end

