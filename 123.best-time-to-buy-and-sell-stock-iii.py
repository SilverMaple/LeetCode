#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import sys
        one_buy = two_buy = sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p-one_buy)
            two_buy = min(two_buy, p-one_profit)
            two_profit = max(two_profit, p-two_buy)
        return two_profit

        # firstBuy, firstSell = -sys.maxsize, 0
        # secondBuy, secondSell = -sys.maxsize, 0
        # for curPrice in prices:
        #     if firstBuy < -curPrice:
        #         firstBuy = -curPrice
        #     if firstSell < firstBuy+curPrice:
        #         firstSell = firstBuy+curPrice
        #     if secondBuy < firstSell-curPrice:
        #         secondBuy = firstSell-curPrice
        #     if secondSell < secondBuy+curPrice:
        #         secondSell = secondBuy+curPrice
        # return secondSell
# @lc code=end

