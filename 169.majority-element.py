#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # return nums[len(nums)//2]

        cnt = 0
        majority = nums[0]
        for num in nums:
            majority = num if cnt==0 else majority
            cnt = cnt+1 if majority==num else cnt-1
        return majority
# @lc code=end

