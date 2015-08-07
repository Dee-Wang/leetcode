# 160 Intersection of Two Linked Lists

## Question:

> Write a program to find the node at which the intersection of two singly linked lists begins.
> 
> 
> For example, the following two linked lists:
> ```
> A:          a1 → a2
>                    ↘
>                      c1 → c2 → c3
>                    ↗          
> B:     b1 → b2 → b3
> ```                
> 
> begin to intersect at node c1.
> 
> 
> *Notes:*
> 
> - If the two linked lists have no intersection at all, return null.
> - The linked lists must retain their original structure after the function returns.
> - You may assume there are no cycles anywhere in the entire linked structure.
> - Your code should preferably run in O(n) time and use only O(1) memory.

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
class Solution
{
    public:
        ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
        {
            int lenA = getListLength(headA);
            int lenB = getListLength(headB);

            if(lenA > lenB)
            {
				int len = lenA - lenB;
				while(len--) headA = headA->next;
            }
            else
            {
				int len = lenB- lenA;
				while(len--) headB = headB->next;
            }

            while(headA)
            {
                if(headA == headB) return headA;
                else
                {
                    headA = headA->next;
                    headB = headB->next;
                }
            }
            return NULL;
        }

    private:
        int getListLength(ListNode *head)
        {
            int result = 0;
            while(head)
            {
                head = head->next;
                result++;
            }
            return result;
        }
};
```
