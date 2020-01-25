#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS
        # squares = [i**2 for i in range(1, int(n**0.5)+1)]
        # d, q, nq = 1, {n}, set()
        # while q:
        #     for node in q:
        #         for square in squares:
        #             if node == square: return d
        #             if node < square: break
        #             nq.add(node-square)
        #     q, nq, d = nq, set(), d+1

        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]
        
# @lc code=end

