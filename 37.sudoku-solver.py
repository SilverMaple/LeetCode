#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.sodoku(board, 0, 0)

    def sodoku(self, A, r, c):
        if c == len(A):
            c = 0
            r += 1

            if r == len(A):
                return True
        
        if A[r][c] != '.':
            return self.sodoku(A, r, c+1)
        for x in range(1, 10):
            if self.check(A, r, c, x):
                A[r][c] = str(x)
                if self.sodoku(A, r, c+1):
                    return True
                A[r][c] = '.'

    def check(self, A, r, c, val):
        # check column
        for x in range(len(A)):
            if A[x][c] == str(val):
                return False
        # check row
        for x in range(len(A)):
            if A[r][x] == str(val):
                return False
        # check submatrix
        top_row = 3 * (r//3)
        top_col = 3 * (c//3)
        for x in range(0, 3):
            for y in range(0,3):
                if A[top_row+x][top_col+y] == str(val):
                    return False
        return True
# @lc code=end

