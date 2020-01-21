#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bsLeft(A, x):
            l, h = 0, len(A)-1
            while l <= h:
                mid = l + (h-l)//2
                if x > A[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
            return l

        def bsRight(A, x):
            l, h = 0, len(A) - 1
            while l <= h:
                mid = l + (h-l)//2
                if x >= A[mid]:
                    l = mid + 1
                else:
                    h = mid - 1
            return h
        
        l, h = bsLeft(nums, target), bsRight(nums, target)
        return (l, h) if l <= h else [-1, -1]
# @lc code=end

