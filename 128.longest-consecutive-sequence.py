#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x-1 not in nums:
                y = x+1
                while y in nums:
                    y+=1
                best = max(best, y-x)
        return best
# @lc code=end

