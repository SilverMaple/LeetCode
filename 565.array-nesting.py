#
# @lc app=leetcode id=565 lang=python
#
# [565] Array Nesting
#

# @lc code=start
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        for i in range(len(nums)):
            cnt = 0
            j = i
            while nums[j] != -1:
                cnt += 1
                nums[j], j = -1, nums[j]
            max_num = max(max_num, cnt)
        return max_num
# @lc code=end

