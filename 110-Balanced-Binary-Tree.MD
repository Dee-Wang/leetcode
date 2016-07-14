# 110 Balanced Binary Tree

## Question:

> Given a binary tree, determine if it is height-balanced.
> 
> For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

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
     bool isBalanced(TreeNode *root) 
     {
        if (!root) return true;
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        if (abs(left_depth - right_depth) <= 1)
            return isBalanced(root->left) && isBalanced(root->right);
        else
            return false;
    }

    int maxDepth(TreeNode* root)
    {
        if (root == NULL) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```
