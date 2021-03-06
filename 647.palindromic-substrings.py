#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # ans = 0
        # for center in range(2*n - 1):
        #     left = center // 2
        #     right = left + center%2
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         ans+=1
        #         left-=1
        #         right+=1
        # return ans

        def manachers(s):
            A = '@#' + '#'.join(s) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A)-1):
                if i < right:
                    Z[i] = min(right-i, Z[2*center-i])
                while A[i+Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] += 1
                if i+Z[i] > right:
                    center, right = i, i+Z[i]
            return Z
        return sum((v+1)//2 for v in manachers(s))
# @lc code=end

