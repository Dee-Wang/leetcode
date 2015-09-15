# 206 Reverse Linked List

## Question:

> Reverse a singly linked list.
> 
> *Hint:*
> A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution:

原链表从头到尾一个个取出来，再用头插法一个个插入到新链表。

## AC Code:
``` javascript
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    var rhead = null;
    while(head){
        var x = head.next;
        head.next = rhead;
        rhead = head;
        head = x;
    }
    return rhead;
};
```
