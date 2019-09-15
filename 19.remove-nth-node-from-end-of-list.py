#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 计算总长度然后直接去除nth
        current = head
        length = 0
        while current is not None:
            current = current.next
            length += 1
        target = length - n
        if target == 0:
            head = head.next
            return head
        current = head
        prev = head
        for i in range(target):
            prev = current
            current = current.next

        prev.next = current.next
        return head

        # 两个节点相隔n-1，一起向前遍历
        # front = head
        # current = head 
        
        # for i in range(n):
        #     front = front.next
        
        # if not front:
        #     return head.next
        
        # while front:
        #     front = front.next
            
        #     if front:
        #         current = current.next
        
        # current.next = current.next.next
        # return head


