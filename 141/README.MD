# 141 Linked List Cycle

## Question:

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

给出一个链表，判断它是否是循环链表。

## Solution:

让快慢指针从链表头开始遍历，快指针向前移动两个位置，慢指针向前移动一个位置

如果快指针到达NULL，说明链表以NULL为结尾，不是循环链表。

如果快指针追上慢指针，则表示出现了循环。

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
    bool hasCycle(ListNode *head) {
        ListNode *fast = head, *slow = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
            if(slow == fast) return true;
        }
        return false;
    }
};
```
