#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for coin in coins:
            for i in range(coin, amount+1):
                if i == coin:
                    dp[i] = 1
                elif dp[i] == 0 and dp[i-coin] != 0:
                    dp[i] = dp[i-coin] + 1
                elif dp[i-coin] != 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[amount] == 0 else dp[amount]

print(Solution().coinChange([1], 0))
# @lc code=end

