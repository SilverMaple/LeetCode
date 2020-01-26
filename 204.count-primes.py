#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_primes = [False]*(n+1)
        count = 0
        for i in range(2, n):
            if not_primes[i]:
                continue
            count += 1
            for j in range(i**2, n, i):
                not_primes[j] = True
        return count

# @lc code=end

