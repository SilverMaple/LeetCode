#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len(text1)
        n2 = len(text2)
        
        # dp = [[0]*(n2+1)]*(n1+1)   # 第二个乘号会使dp[0],d[1]和dp[2]都指向同一内存空间，id(dp[0])==id(dp[1])
        # dp = [[0] * (n2+1) for _ in range(n1+1)]  # √
        dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                a, b = text1[i], text2[j]
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1-1][n2-1]

print(\
    Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
# @lc code=end

