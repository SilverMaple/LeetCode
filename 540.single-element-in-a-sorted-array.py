#
# @lc app=leetcode id=540 lang=python
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        while l < h:
            m = l + (h-l) // 2
            if m%2 == 1:
                m -= 1
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                h = m
        return nums[l]        
# @lc code=end

