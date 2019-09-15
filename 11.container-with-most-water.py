#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # Time complexity : O(n). Single pass.
        # Space complexity : O(1). Constant space is used.
        # √ 50/50 cases passed (104 ms)
        # √ Your runtime beats 68.29 % of python submissions
        # √ Your memory usage beats 32.2 % of python submissions (13.1 MB)
        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            max_area = max((end-start) * min(height[start], height[end]), max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area

