#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left, right = self.minDepth(root.left), self.minDepth(root.right)
        if left==0 or right==0:
            return left+right+1
        return min(left, right)+1
# @lc code=end

