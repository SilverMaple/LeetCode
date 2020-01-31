#
# @lc app=leetcode id=766 lang=python
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # return all(r1[:-1] == r2[1:] for r1,r2 in zip(matrix, matrix[1:]))
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
# @lc code=end

