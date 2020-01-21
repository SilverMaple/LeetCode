#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1 if nums else 0
        for i in nums[1:]:
            if i != nums[index-1]:
                nums[index] = i
                index += 1
        return index
