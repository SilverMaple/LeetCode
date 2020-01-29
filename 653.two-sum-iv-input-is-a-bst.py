#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
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
        l, h = 0, len(arr)-1
        while l < h:
            two_sum = arr[l] + arr[h]
            if two_sum == k:
                return True
            elif two_sum < k:
                l += 1
            elif two_sum > k:
                h -= 1
        return False
# @lc code=end

