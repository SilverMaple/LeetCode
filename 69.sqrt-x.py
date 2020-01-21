#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        l, h = 1, x
        while l <= h:
            mid = l + int((h-l) / 2)
            sqrt = int(x / mid)
            if sqrt == mid:
                return mid
            elif mid > sqrt:
                h = mid - 1
            else:
                l = mid + 1
        return h
# @lc code=end

