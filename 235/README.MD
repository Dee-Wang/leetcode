# 235 Lowest Common Ancestor of a Binary Search Tree

## Question:

> Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
> 
> According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
> 
> ```
>         _______6______
>        /              \
>     ___2__          ___8__
>    /      \        /      \
>    0      _4       7       9
>          /  \
>          3   5
> ```
>          
> For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

给出一颗二叉查找树，寻找两个节点的最近公共祖先。

## Solution:

递归:

+ 若p或q为root，则root为最近公共祖先
+ 若p,q都在root左边，则继续在root的左子树中寻找
+ 若p,q都在root右边，则继续在root的右子树中寻找
+ 若p,q分别在root的左右子树中，则root为最近公共祖先

## AC Code:
``` c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
         if (root->val == p->val || root->val == q->val) return root;
         bool b1 = root->val > p->val, b2 = root->val > q->val;
         if(b1 && b2) return lowestCommonAncestor(root->left,p,q);
         else if(!b1 && !b2) return lowestCommonAncestor(root->right,p,q);
         else return root;
    }
};
```
