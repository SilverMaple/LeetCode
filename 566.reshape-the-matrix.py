#
# @lc app=leetcode id=566 lang=python
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        import numpy as np
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
# @lc code=end

