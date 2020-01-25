#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob1(nums, 0, n-2), self.rob1(nums, 1, n-1))

    def rob1(self, nums, first, last):
        pre2, pre1 = 0, 0
        for i in range(first, last+1):
            cur = max(pre1, pre2+nums[i])
            pre2 = pre1
            pre1 = cur
        return pre1
# @lc code=end

