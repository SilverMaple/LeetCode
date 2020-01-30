#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        return [s.find(i) for i in s] == [t.find(j) for j in t]
# @lc code=end

