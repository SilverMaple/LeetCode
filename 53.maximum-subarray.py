#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        preSum = nums[0]
        maxSum = preSum
        for num in nums[1:]:
            preSum = max(num, preSum+num)
            maxSum = max(maxSum, preSum)
        return maxSum
# @lc code=end

