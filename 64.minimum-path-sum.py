#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j]
                elif i == 0:
                    dp[j] = dp[j-1]
                else:
                    dp[j] = min(dp[j-1], dp[j])
                dp[j] += grid[i][j]

        return dp[n-1]
# @lc code=end

