#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 头插法
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev

        if not head or not head.next:
            return head
        next_node = head.next
        new_head = self.reverseList(next_node)
        next_node.next = head
        head.next = None
        return new_head
# @lc code=end

