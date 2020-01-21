#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l < h:
            m = l + (h-l)//2
            if nums[m] <= nums[h]:
                h = m
            else:
                l = m+1
        return nums[l]
# @lc code=end

