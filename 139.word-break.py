#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [True] + [False]*n
        for i in range(1, n+1):
            for word in wordDict:
                length = len(word)
                if length <= i and word == s[i-length: i]:
                    dp[i] = dp[i] or dp[i-length]

        return dp[n]
Solution().wordBreak('ssdfa', {'asfd', 'sdfs'})
# @lc code=end

