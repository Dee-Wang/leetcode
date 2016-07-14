# 83 Remove Duplicates from Sorted List

## Question:

> Given a sorted linked list, delete all duplicates such that each element appear only once.
> 
> For example,
>
> Given ```1->1->2```, return ```1->2```.
>
> Given ```1->1->2->3->3```, return ```1->2->3```.

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
    ListNode *deleteDuplicates(ListNode *head) {
        if(!head) return NULL;
        int lastVal = head->val;
        ListNode *p = head;
        while(p->next)
        {
            if(p->next->val == lastVal)
            {
                p->next = p->next->next;
            }else{
                lastVal = p->next->val;
                p = p->next;
            }
        }
        return head;
    }
};
```
