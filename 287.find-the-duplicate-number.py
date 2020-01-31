#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 1, len(nums)-1
        while l<=h:
            mid = l + (h-l)//2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt += 1
            if cnt > mid:
                h = mid-1
            else:
                l = mid+1
        return l
# @lc code=end

