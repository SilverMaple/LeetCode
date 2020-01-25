#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if k >= n/2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i]-prices[i-1]
            return max_profit
        profits = [0]*n
        for j in range(k):
            pre_profit = 0
            for i in range(1, n):
                profit = prices[i] - prices[i-1]
                pre_profit = max(pre_profit+profit, profits[i])
                profits[i] = max(profits[i-1], pre_profit)

        return profits[-1]

        # n = len(prices)
        # if k >= n/2:
        #     max_profit = 0
        #     for i in range(1, n):
        #         if prices[i] > prices[i-1]:
        #             max_profit += prices[i]-prices[i-1]
        #     return max_profit
        # max_profit = [[0]*n for _ in range(k+1)]
        # for i in range(1, k+1):
        #     local_max = max_profit[i-1][0] - prices[0]
        #     for j in range(1, n):
        #         max_profit[i][j] = max(max_profit[i][j-1], prices[j]+local_max)
        #         local_max = max(local_max, max_profit[i-1][j]-prices[j])

        # return max_profit[k][n-1]
# @lc code=end

