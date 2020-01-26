#
# @lc app=leetcode id=628 lang=python
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
        
        # import heapq
        # a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        # return max(a[0]*a[1]*a[2], b[0]*b[1]*a[0])

        import sys
        max1 = max2 = max3 = -sys.maxsize
        min1 = min2 = min3 = sys.maxsize
        for num in nums:
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num

            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
        return max(max1*max2*max3, max1*min1*min2)
# @lc code=end

