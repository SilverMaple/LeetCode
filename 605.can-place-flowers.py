#
# @lc app=leetcode id=605 lang=python
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(flowerbed):
            if not x and (i == 0 or flowerbed[i-1] == 0) \
                and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
        return n <= 0
# @lc code=end

