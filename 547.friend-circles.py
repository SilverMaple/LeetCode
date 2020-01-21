#
# @lc app=leetcode id=547 lang=python
#
# [547] Friend Circles
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        seen = set()
        def dfs(node):
            for i, adj in enumerate(M[node]):
                if adj and i not in seen:
                    seen.add(i)
                    dfs(i)
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
# @lc code=end

