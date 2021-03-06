#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j*dp[i-j], j*(i-j)))
        return dp[n]
# @lc code=end

