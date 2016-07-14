# 2 Add Two Numbers

## Question:

> You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
> 
> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
> 
> Output: 7 -> 0 -> 8

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
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	if(l1 == NULL && l2 == NULL) return NULL;
	if(l1 == NULL) return l2;
	if(l2 == NULL) return l1;
	ListNode *lr = new ListNode(0);
	ListNode *p = lr;
	int carry = 0, num;
	while(l1 != NULL || l2 != NULL || carry){
	  num = 0;
	  if(l1) {
		num += l1->val;
		l1 = l1->next;
	  }
	  if(l2) {
		num += l2->val;
		l2 = l2->next;
	  }
	  if(carry){
		num += carry;
		carry = 0;
	  }
	  if(num > 9) {
		carry = num / 10;
		num %= 10;
	  }
	  p->next = new ListNode(num);
	  p = p->next;
	}
	p = lr;
	lr = lr->next;
	delete p;
	return lr;
  }
};
```
