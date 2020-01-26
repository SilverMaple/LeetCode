#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        products = [1]*n
        left = 1
        for i in range(1, n):
            left *= nums[i-1]
            products[i] *= left
        right = 1
        for i in range(n-2, -1, -1):
            right *= nums[i+1]
            products[i] *= right
        return products
# @lc code=end

