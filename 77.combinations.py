#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # if k == 0:
        #     return [[]]
        # return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        res = []
        self.dfs(n, k, [], res)
        return res

    def dfs(self, n, k, path, res):
        if len(path) == k:
            res.append(path)
        start = max(len(path)+1, max(path) if path else -1)
        for i in range(start, n+1):
            if i in path:
                continue
            self.dfs(n, k, path+[i], res)

print(Solution().combine(3, 2))
# @lc code=end

