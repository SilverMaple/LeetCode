#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        self.dfs(root, str(root.val), res)
        return res
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append(path)
        if node.left:
            self.dfs(node.left, path+'->'+str(node.left.val), res)
        if node.right:
            self.dfs(node.right, path+'->'+str(node.right.val), res)

# @lc code=end

