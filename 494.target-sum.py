#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#

# @lc code=start
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = sum(nums)
        if sums < S or (sums+S)%2 == 1:
            return 0
        w = (sums+S) / 2
        dp = [1] + [0]*w
        for num in nums:
            for i in range(w, num-1, -1):
                dp[i] = dp[i] + dp[i-num]

        return dp[w]
# @lc code=end

