#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head.next
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        else:
            head = None
        
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node
# @lc code=end

