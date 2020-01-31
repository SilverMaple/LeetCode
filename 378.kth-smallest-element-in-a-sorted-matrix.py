#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo <= hi:
            mid = lo + (hi-lo)//2
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] > mid:
                        break
                    cnt += 1
            if cnt < k:
                lo = mid+1
            else:
                hi = mid-1
        return lo
# @lc code=end

