#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre2, pre1 = 0, 0
        for i in range(len(nums)):
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return pre1
# @lc code=end

