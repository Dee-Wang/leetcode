# 100 Same Tree

## Question:

> Given two binary trees, write a function to check if they are equal or not.
> 
> Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
> 
> 给出两个二叉树，写个方法检查这两棵树是否相等。
> 
> 两个二叉树相等意味着结构相同，而且值也相等。

## Solution:

递归：

+ 若pq两树都为空，则返回true
+ 若q树空但p树不为空，则返回false
+ 若p树空但q树不为空，则返回false
+ 若pq两树根节点值不相等，则返回false
+ 若pq两树的左子树不相等，则返回false
+ 若pq两树的右子树不相等，则返回false
+ 以上条件都通过，直接返回true

## AC Code:

``` c++
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if(p==NULL&&q==NULL) return true;
        if(p==NULL&&q!=NULL) return false;
        if(p!=NULL&&q==NULL) return false;
        if(p->val != q->val) return false;
        if(!isSameTree(p->left,q->left)) return false;
        if(!isSameTree(p->right, q->right)) return false;
        return true;
    }
};
```
