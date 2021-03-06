#
# @lc app=leetcode id=665 lang=python
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(1, len(nums)):
            if count >= 2:
                break
            if nums[i] >= nums[i-1]:
                continue
            count += 1
            if i-2 >= 0 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]

        return count <= 1
# @lc code=end

