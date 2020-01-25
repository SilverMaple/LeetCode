#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        maximun = [1] + [0]*target
        nums.sort()
        for i in range(1, target+1):
            for j in range(0, len(nums)):
                if nums[j] > i:
                    break
                maximun[i] += maximun[i-nums[j]]
        return maximun[target]
# @lc code=end

