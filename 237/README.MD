# 237 Delete Node in a Linked List

## Question:

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

删除单链表中给定的节点

## Solution:

单链表删除节点的一般步骤是先将前一节点的next指向后一节点，然后删除这个节点，但是这里只给出了当前节点的指针，显然不能访问到前一节点，但是可以将下一节点的值赋给当前节点，然后将当前节点的next指向下下个节点。

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
    void deleteNode(ListNode* node) {
         node->val = node->next->val;
         node->next = node->next->next;
    }
};
```
