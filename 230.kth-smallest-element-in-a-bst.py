#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.val = 0
        def inOrder(node, k):
            if not node:
                return
            inOrder(node.left, k)
            self.count += 1
            if self.count == k:
                self.val = node.val
                return
            inOrder(node.right, k)

        inOrder(root, k)
        return self.val
# @lc code=end

