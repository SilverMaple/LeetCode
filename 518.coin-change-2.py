#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change 2
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if not coins:
            return 0
        dp = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]
# @lc code=end

