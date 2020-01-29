#
# @lc app=leetcode id=530 lang=python
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            arr.append(node.val)
            cur = node.right
        return min(abs(arr[i]-arr[i+1]) for i in range(len(arr)-1))
# @lc code=end

