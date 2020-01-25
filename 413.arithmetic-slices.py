#
# @lc app=leetcode id=413 lang=python
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A) == 0:
            return 0
        n = len(A)
        dp = [0] * n
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1

        total = 0
        for cnt in dp:
            total += cnt
        return total
# @lc code=end

