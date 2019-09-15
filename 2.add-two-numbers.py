#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.67%)
# Total Accepted:    783.9K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # √ Your runtime beats 20.8 % of python submissions
        # √ Your memory usage beats 5.16 % of python submissions (11.1 MB)
        # list_head = ListNode(0)
        # list_tail = list_head
        # add_on = 0
        # while(l1 is not None or l2 is not None):
        #     list_tmp = ListNode(add_on)
        #     print(add_on)
        #     list_tail.next = list_tmp
        #     if l1 is not None:
        #         list_tmp.val += l1.val
        #         l1 = l1.next
        #     if l2 is not None:
        #         list_tmp.val += l2.val
        #         l2 = l2.next
        #     add_on = int(list_tmp.val / 10)
        #     list_tmp.val %= 10
        #     list_tail = list_tmp
        # if add_on is not 0:
        #     list_tmp = ListNode(add_on)
        #     list_tail.next = list_tmp
        # return list_head.next

        # √ Your runtime beats 89.31 % of python submissions
        # √ Your memory usage beats 84.1 % of python submissions (10.8 MB)
        ''' Decompose the task into pieces that reduces unnecessary calculation'''
        add_all = l1.val + l2.val
        add_on = int(add_all / 10)
        list_tail = list_head = ListNode(add_all % 10)
        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            add_all = l1.val + l2.val + add_on
            add_on = int(add_all / 10)
            list_tmp = ListNode(add_all % 10)
            list_tail.next = list_tmp
            list_tail = list_tmp
            l1 = l1.next
            l2 = l2.next
        
        if l1 is not None:
            list_longer = l1
        else:
            list_longer = l2

        while add_on is not 0 and list_longer is not None:
            add_all = list_longer.val + add_on
            add_on = int(add_all / 10)
            list_tmp = ListNode(add_all % 10)
            list_tail.next = list_tmp
            list_tail = list_tmp
            list_longer = list_longer.next

        if add_on is not 0 and list_longer is None:
            list_tmp = ListNode(add_on)
            list_tail.next = list_tmp
            list_tail = list_tmp
        
        if add_on is 0 and list_longer is not None:
            while list_longer is not None:
                list_tmp = ListNode(list_longer.val)
                list_tail.next = list_tmp
                list_tail = list_tmp
                list_longer = list_longer.next

        # while(list_head is not None):
        #     print(list_head.val)
        #     list_head = list_head.next
        return list_head
        
# l1 = ListNode(2)
# l1_2 = ListNode(4)
# l1_3 = ListNode(3)
# l1_2.next = l1_3
# l1.next = l1_2

# l2 = ListNode(5)
# l2_2 = ListNode(6)
# l2_3 = ListNode(4)
# l2_2.next = l2_3
# l2.next = l2_2
# s = Solution()
# s.addTwoNumbers(l1, l2)
