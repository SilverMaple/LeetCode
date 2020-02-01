#
# @lc app=leetcode id=684 lang=python
#
# [684] Redundant Connection
#

# @lc code=start
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # tree = ''.join(map(chr, range(1001)))
        tree = ''.join(map(unichr, range(1001)))
        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]
            tree = tree.replace(tree[u], tree[v])
# @lc code=end

