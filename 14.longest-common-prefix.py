#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # √ 118/118 cases passed (16 ms)
        # √ Your runtime beats 91.5 % of python submissions
        # √ Your memory usage beats 82.5 % of python submissions (11.9 MB)
        if len(strs) == 0:
            return ''
        strs.sort()
        i = 0
        while len(strs[0]) > i and len(strs[-1]) > i:
            if strs[0][i] == strs[-1][i]:
                i += 1
            else:
                break
        return strs[0][:i]

        # niubi   
        # if not strs: return ""
        # l, h = min(strs), max(strs)
        # return l[:next((i for i in range(len(l)) if l[i] != h[i]), len(l))]

