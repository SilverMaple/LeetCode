#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while start != end:
            cur = numbers[start] + numbers[end]
            if cur == target:
                return [start+1, end+1]
            elif cur < target:
                start += 1
            else:
                end -= 1
        return None
# @lc code=end

