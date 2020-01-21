#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)

        # def kmp(str_):
        #     b, prefix = 0, [0]
        #     for i in range(1, len(str_)):
        #         while b > 0 and str_[i] != str_[b]:
        #             b = prefix[b - 1]
        #         if str_[b] == str_[i]:
        #             b += 1
        #         else:
        #             b = 0
        #         prefix.append(b)
        #     return prefix

        # str_ = kmp(needle + '#' + haystack)
        # n = len(needle)
        # if n == 0:
        #     return n
        # for i in range(n + 1, len(str_)):
        #     if str_[i] == n:
        #         return i - 2 * n
        # return -1

        S, T = haystack, needle
        if not T: return 0
        
        b = [0] * (len(T) + 1)
        i, j = 0, -1
        b[i] = j
        # prepare roll-back table
        while i < len(T):
            # roll-back
            while j >= 0 and T[i] != T[j]: j = b[j]
            i, j = i + 1, j + 1
            b[i] = j
        
        i = j = 0
        while i < len(S):
            # roll-back
            while j >= 0 and T[j] != S[i]: j = b[j]
            i, j = i + 1, j + 1
            if j == len(T): return i - len(T)
        return -1

        

