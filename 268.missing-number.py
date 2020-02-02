#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 98% speed
        # return sum(range(len(nums)+1)) - sum(nums) if 0 in nums else 0
        
        # 58% speed
        ret = 0
        for i in range(len(nums)):
            ret = ret ^ i ^ nums[i]
        return ret ^ len(nums)
# @lc code=end

