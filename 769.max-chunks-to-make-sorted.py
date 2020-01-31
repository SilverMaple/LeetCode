#
# @lc app=leetcode id=769 lang=python
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        ret = 0
        right = arr[0]
        for i in range(len(arr)):
            right = max(right, arr[i])
            if right == i:
                ret+=1
        return ret
# @lc code=end

