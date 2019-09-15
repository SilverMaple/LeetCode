#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()                
        result = sum(nums[:3])      
        numsLen = len(nums)
        diff = abs(result - target) 

        for i in range(numsLen):
            left, right = i + 1, numsLen - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                curDiff = abs(total - target)

                if curDiff < diff:
                    diff = curDiff
                    result = total

                if total < target:   
                    left += 1
                elif total > target: 
                    right -= 1
                else:                
                    return result

        return result
        