#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.01%)
# Total Accepted:    827.3K
# Total Submissions: 3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # √ Your runtime beats 58.2 % of python submissions
        # √ Your memory usage beats 14.6 % of python submissions (12 MB)
        # index = 0
        # length = 0
        # # max_index = 0
        # max_length = 0
        # for i in range(len(s)):
        #     j = s.index(str(s[i]), index, len(s))
        #     if j is not -1 and j < i:
        #         length = length - (j - index)
        #         index = j + 1
        #     else:
        #         length += 1
        #     if length > max_length:
        #         # max_index = index
        #         max_length = length
        # #     print(index, length)
        # # print(s[max_index: max_index+max_length])
        # return max_length

        # √ Your runtime beats 94.14 % of python submissions
        # √ Your memory usage beats 42.3 % of python submissions (11.4 MB)
        # d = ''
        # f = ''
        # for i in s:
        #     if i not in f:
        #         f += i
        #     else:
        #         if len(d) < len(f):
        #             d = f
        #         f = f[f.index(i)+1::] + i
        # # print(max(len(d), len(f)))
        # return max(len(d), len(f))

        # √ Your runtime beats 99.31 % of python submissions
        # √ Your memory usage beats 77 % of python submissions (11.1 MB)
        '''When change array slice operation form [::] to [:], runtime and memory usage improve a lot'''
        d = ''
        f = ''
        for i in s:
            if i not in f:
                f += i
            else:
                if len(d) < len(f):
                    d = f
                f = f[f.index(i)+1:] + i
        return max(len(d), len(f))


# s = Solution()
# s.lengthOfLongestSubstring('pwwkew')
# s.lengthOfLongestSubstring('dvdf')
