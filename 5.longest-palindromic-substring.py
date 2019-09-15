#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.72%)
# Total Accepted:    492.6K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''Dynamic programming: P(i,j) = (P(i+1, j-1) and Si == Sj)'''
        '''                     P(i,i+1) = (Si == Si+1)'''
        # Runtime: 980 ms, faster than 52.21% of Python online submissions.
        # Memory Usage: 10.8 MB, less than 53.28% of Python online submissions.
        # index = 0
        # max_span = 0
        # span = 0
        # # odd
        # for i in range(len(s)):
        #     while i-span >= 0 and i+span < len(s) and s[i-span] == s[i+span]:
        #         span += 1
        #     if span is not 0 and span >= max_span:
        #         index = i
        #         max_span = span
        #     span = 0
        # result = s[index-max_span+1: index+max_span]
        # # even
        # for i in range(len(s)):
        #     while i-span >= 0 and i+span+1 < len(s) and s[i-span] == s[i+span+1]:
        #         span += 1
        #     if span is not 0 and span*2 >= max_span*2-1:
        #         index = i
        #         max_span = span
        #         result = s[index-max_span+1:index+max_span+1]
        #     span = 0
        # return result

        # Runtime: 60 ms, faster than 96.27% of Python online submissions.
        # Memory Usage: 10.8 MB, less than 63.46% of Python online submissions.
        if len(s) <= 1:
            return s
        s_temp = "$#"+ '#'.join(list(s)) + "#&"
        temp_len = len(s_temp)
        P = [0 for i in range(temp_len - 1)]
        P[0], P[1] = 1 ,1
        mx, center = 3, 2
        rescenter, maxlen = 1, 1
        for i in range(2, temp_len - 1):
            P[i] = min(P[2*center - i], mx - i) if mx > i else 1
            while s_temp[i + P[i]] == s_temp[i - P[i]]:
                P[i] += 1
            if(mx < i + P[i]):
                mx = i + P[i]
                center = i
            if(maxlen < P[i]):
                rescenter = i
                maxlen = P[i]
        start = int((rescenter - maxlen) / 2)
        return s[start:start + maxlen - 1]
        
s = Solution()
print(s.longestPalindrome('basdfdsb'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('babad'))
