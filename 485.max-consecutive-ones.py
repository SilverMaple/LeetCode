#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, cur = 0, 0
        for x in nums:
            cur = 0 if x == 0 else cur + 1
            maximum = max(maximum, cur)
        return maximum
        
# @lc code=end

