#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            ret ^= n
        return ret
# @lc code=end

