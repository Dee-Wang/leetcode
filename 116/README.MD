# 116 Populating Next Right Pointers in Each Node

## Question:

> Given a binary tree
> 
> 
>     struct TreeLinkNode {
>       TreeLinkNode *left;
>       TreeLinkNode *right;
>       TreeLinkNode *next;
>       }
> 
> Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
> 
> Initially, all next pointers are set to NULL.
> 
> Note:
> 
> You may only use constant extra space.
> You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
> For example,
> Given the following perfect binary tree,
> 
>          1
>        /  \
>       2    3
>      / \  / \
>      4  5  6  7
> 
> After calling your function, the tree should look like:
> 
>          1 -> NULL
>        /  \
>       2 -> 3 -> NULL
>      / \  / \
>     4->5->6->7 -> NULL

将一个完全二叉树的每一层连接起来

## Solution:

递归:

+ 若根节点为空，直接返回
+ 若不为叶子节点，左孩子的next指向右孩子，若root的next不为空，右孩子的next指向root->next的左孩子
+ 连接左子树
+ 连接右子树

## AC Code:

``` c++
/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        if(root->left) {
            root->left->next = root->right;
            if(root->next) root->right->next = root->next->left;
        }
        connect(root->left);
        connect(root->right);
    }
};
```
