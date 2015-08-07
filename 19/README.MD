# 19 Remove Nth Node From End of List

## Question:

> Given a linked list, remove the n^th node from the end of list and return its head.
> 
> For example,
> 
> > Given linked list: 1->2->3->4->5, and n = 2.
> > 
> > After removing the second node from the end, the linked list becomes 1->2->3->5.
> 
> *Note:*
> 
> Given n will always be valid.
> 
> Try to do this in one pass.

## AC Code:

``` c++
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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        int len = 0;
        ListNode *p = head;
        while(p)
        {
            len++;
            p = p->next;
        }
        n = len - n;
        p = head;
        if(!n) 
        {
            head = head->next;
        }
        else
        {
            while(--n) p = p->next;
            ListNode *q = p;
            p = p->next;
            q->next = p->next;
        }
        delete p;
        p = NULL;
        return head;
    }
};
```
