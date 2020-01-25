#
# @lc app=leetcode id=650 lang=python
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==1:
        #     return 0
        # for i in range(2, int(n**0.5)+1):
        #     if n%i == 0:
        #         return i+self.minSteps(n/i)
        # return n

        dp = [0]*(n+1)
        h = int(n**0.5)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(2, h+1):
                if i%j == 0:
                    dp[i] = dp[j] + dp[int(i/j)]
                    break
        return dp[n]
print(Solution().minSteps(5))
# @lc code=end

