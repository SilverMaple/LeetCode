#
# @lc app=leetcode id=503 lang=python
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        next_nums = [-1]*n
        pre = []
        for i in range(n*2):
            num = nums[i%n]
            while pre and nums[pre[-1]] < num:
                next_nums[pre.pop()] = num
            if i<n:
                pre.append(i)
        return next_nums
# @lc code=end

