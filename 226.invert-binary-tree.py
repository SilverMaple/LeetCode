#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        leftNode = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(leftNode)
        return root
# @lc code=end

