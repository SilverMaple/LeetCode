#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def pathSumRoot(root, sum):
            if not root:
                return 0
            ret = 0
            if root.val == sum:
                ret += 1

            ret += pathSumRoot(root.left, sum-root.val)
            ret += pathSumRoot(root.right, sum-root.val)
            return ret

        if not root:
            return 0
        return pathSumRoot(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

        
# @lc code=end

