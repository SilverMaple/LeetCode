#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def travel(node):
            if not node:
                return
            travel(node.right)
            self.sum += node.val
            node.val = self.sum
            travel(node.left)

        travel(root)
        return root
# @lc code=end

