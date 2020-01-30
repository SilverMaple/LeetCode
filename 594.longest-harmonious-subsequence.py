#
# @lc app=leetcode id=594 lang=python
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans

# @lc code=end

