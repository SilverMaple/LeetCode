/*
 * @lc app=leetcode id=141 lang=cpp
 *
 * [141] Linked List Cycle
 */
#include <cstddef>
#include <exception>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
 };

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) {
            return false;
        }
        ListNode *l1 = head, *l2 = head->next;
        while(l2!=NULL && l2->next!=NULL) {
            if (l1 == l2)
                return true;
            l1 = l1->next;
            l2 = l2->next->next;
        }
        return false;
    }
};
// @lc code=end

