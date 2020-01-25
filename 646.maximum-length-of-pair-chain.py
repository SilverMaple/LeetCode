#
# @lc app=leetcode id=646 lang=python
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        n = len(pairs)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1

        return max(dp)
# @lc code=end

