#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
        for i in range(1, len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
    
    def isPar(self, s):
        return s == s[::-1]
# @lc code=end

