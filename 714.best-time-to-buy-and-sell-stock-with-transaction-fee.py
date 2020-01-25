#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices or len(prices) == 0:
            return 0
        n = len(prices)
        buy, s1, sell, s2 = [0]*n, [0]*n, [0]*n, [0]*n
        s1[0], buy[0] = -prices[0], -prices[0]
        sell[0], s2[0] = 0, 0
        for i in range(1, n):
            buy[i] = max(s2[i-1], sell[i-1]) - prices[i]
            s1[i] = max(buy[i-1], s1[i-1])
            sell[i] = max(buy[i-1], s1[i-1]) + prices[i] - fee
            s2[i] = max(s2[i-1], sell[i-1])
        return max(sell[n-1], s2[n-1])
# @lc code=end

