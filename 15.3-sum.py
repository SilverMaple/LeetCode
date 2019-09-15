#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        l = len(nums)
        if l>3:
            res = []
            nums.sort()
            res = []
            for i in range(l-2):
                left, right = i+1, l-1
                if i>0 and nums[i]==nums[i-1]:
                    continue
                while left<right:
                    s = nums[i]+nums[left]+nums[right]
                    if s<0:
                        left += 1
                    elif s>0:
                        right -= 1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left += 1
                        while left<right and nums[right]==nums[right-1]:
                            right -= 1
                        left, right = left+1, right-1
            return res
        elif l == 3:
            if sum(nums) == 0:
                return [nums]

