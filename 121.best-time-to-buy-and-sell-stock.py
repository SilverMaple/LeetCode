#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        soFarMin = prices[0]
        maxP = 0
        for i in range(1, len(prices)):
            if soFarMin > prices[i]:
                soFarMin = prices[i]
            else:
                maxP = max(maxP, prices[i] - soFarMin)
        return maxP
# @lc code=end

