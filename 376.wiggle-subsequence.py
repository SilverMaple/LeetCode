#
# @lc app=leetcode id=376 lang=python
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        up, down = 1, 1
        for i in range(len(nums)):
            if nums[i] > nums[i-1]:
                up = down+1
            elif nums[i] < nums[i-1]:
                down = up+1
        
        return max(up, down)
# @lc code=end

