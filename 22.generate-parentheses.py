#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # backtracking
        # 回溯法主要通过类似决策树过程逐层寻找有效解，正向方法？
        # res = []
        # def backtracking(left, right, cur):
        #     if left == n and right == n:
        #         res.append(cur)
        #         return
        #     if left < n:
        #         cur += '('
        #         backtracking(left+1, right, cur)
        #         cur = cur[:-1]
        #     if right < left:
        #         cur += ')'
        #         backtracking(left, right+1, cur)
        # backtracking(0, 0, '')
        # return res

        # Dynamic Program，第一次想是dp方法但没找到这个规律
        # 如果能找到规律动态规划很好理解和实现
        dp = [None for i in range(n+1)]

        def recur(n):
            if n == 0:
                return ['']
            if n == 1:
                return ['()']
            if dp[n] is not None:
                return dp[n]
            ans = []
            for i in range(n):
                for left in recur(i):
                    for right in recur(n-i-1):
                        ans.append('({}){}'.format(left, right))
            dp[n] = ans
            return ans
        return recur(n)

