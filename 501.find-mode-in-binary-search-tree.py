#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
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
        ret = [(i, arr.count(i)) for i in set(arr)]
        ret.sort(key=lambda x: x[1])
        
        return [x[0] for x in list(filter(lambda x:x[1]==ret[-1][1], ret))] if ret else None
# @lc code=end

