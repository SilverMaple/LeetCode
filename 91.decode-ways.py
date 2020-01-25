#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            one = int(s[i-1])
            if 0 < one and one <= 9:
                dp[i] += dp[i-1]
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]

print(Solution().numDecodings('12'))
# @lc code=end

