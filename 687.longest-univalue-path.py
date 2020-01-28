#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.path = 0
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            leftPath = left+1 if root.left and root.left.val==root.val else 0
            rightPath = right+1 if root.right and root.right.val==root.val else 0
            self.path = max(self.path, leftPath + rightPath)
            return max(leftPath, rightPath)

        dfs(root)
        return self.path
# @lc code=end

