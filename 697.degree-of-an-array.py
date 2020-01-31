#
# @lc app=leetcode id=697 lang=python
#
# [697] Degree of an Array
#

# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            deg = max(deg, len(nums_map[num]))
        for num, indies in nums_map.items():
            if len(indies) == deg:
                min_len = min(min_len, indies[-1]-indies[0]+1)
        return min_len
# @lc code=end

