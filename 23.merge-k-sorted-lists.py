#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


        # 每次都排序，超时
        # if len(lists)<1:
        #     return None 

        # head = ListNode(0)
        # current = head
        # lists = [node for node in lists if node]
        # while len(lists)>0:
        #     lists = sorted(lists, key=lambda x: x.val)
        #     current.next = lists[0]
        #     lists[0] = lists[0].next
        #     current = current.next
        #     lists = [node for node in lists if node]

        # return head.next

        # 最小堆, 108ms
        import heapq
        head = ListNode(0)
        heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        for i in range(len(lists)):
            lists[i] = lists[i].next if lists[i] else None
        heapq.heapify(heap)

        cur = head
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

        # 优先级队列 172ms
        # from Queue import PriorityQueue
        # dummy = ListNode(None)
        # current = dummy
        # q = PriorityQueue()
        # for node in lists:
        #     if node: q.put((node.val, node))
        # while q.qsize()>0:
        #     current.next = q.get()[1]
        #     current = current.next
        #     if current.next: q.put((current.next.val, current.next))
        # return dummy.next

