#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(None)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    # 交换三个引用，分开写的话需要temp变量交换
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
