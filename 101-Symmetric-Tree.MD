# 101 Symmetric Tree 

## Question:

> Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
> 
> For example, this binary tree is symmetric:
> 
> ```
>     1
>    / \
>   2   2
>  / \ / \
> 3  4 4  3
> ```
> But the following is not:
> ```
>     1
>    / \
>   2   2
>    \   \
>    3    3
> ```
> Note:
> Bonus points if you could solve it both recursively and iteratively.

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
    bool isSymmetric(TreeNode *root) {
        if(root == NULL) return true;
        if(isSymmetricTree(root->left,root->right)) return true;
        else return false;
    }
    
    bool isSymmetricTree(TreeNode *p, TreeNode *q)
    {
        if(p==NULL&&q==NULL) return true;
        if(p==NULL&&q!=NULL) return false;
        if(p!=NULL&&q==NULL) return false;
        if(p->val != q->val) return false;
        if(!isSymmetricTree(p->left,q->right)) return false;
        if(!isSymmetricTree(q->left,p->right)) return false;
        return true;
    }
};
```
