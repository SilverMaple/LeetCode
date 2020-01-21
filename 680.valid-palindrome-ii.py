#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        def isPalin(s):
            return s==s[::-1] 
            
        while l<r:
            if s[l]!=s[r]:
                return isPalin(s[l+1:r+1]) or isPalin(s[l:r])
            l += 1
            r -= 1
        return True
# @lc code=end

