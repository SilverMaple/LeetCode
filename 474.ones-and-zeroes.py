#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # prev = [[0]*(n+1) for _ in range(m+1)]
        # curr = [[0]*(n+1) for _ in range(m+1)]
        # for i in range(1, len(strs)+1):
        #     zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')
        #     for j in range(m+1):
        #         for k in range(n+1):
        #             curr[j][k] = 0
        #             if j >= zeros and k >= ones:
        #                 curr[j][k] = max(prev[j][k], 1+prev[j-zeros][k-ones])
        #             else:
        #                 curr[j][k] = prev[j][k]
        #     prev, curr = curr, prev
        # return prev[m][n]

        # dp = [[0]*(n+1)]*(m+1)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)

        return dp[m][n]
# @lc code=end

