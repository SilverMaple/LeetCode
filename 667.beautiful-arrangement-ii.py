#
# @lc app=leetcode id=667 lang=python
#
# [667] Beautiful Arrangement II
#

# @lc code=start
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = range(1, n-k)
        for d in range(k+1):
            if d%2 == 0:
                ans.append(n-k+ d/2)
            else:
                ans.append(n - d//2)
        return ans
# @lc code=end

