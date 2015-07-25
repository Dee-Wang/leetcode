# 104 Maximum Depth of Binary Tree

## Question:

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

给出一个二叉树，找出这棵树的最大深度。

最大深度就是叶子节点到根节点的最长路径。

## Solution:

递归：

+ 若当前节点为叶子节点，则返回0
+ 若当前节点不为叶子节点，其最大深度为左右子树的最大深度+1

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
    int maxDepth(TreeNode *root) {
        if(root == NULL) return 0;
        int left_depth = 0, right_depth = 0;
        if(root->left) left_depth = maxDepth(root->left);
        if(root->right) right_depth = maxDepth(root->right);
        return left_depth>right_depth?left_depth+1:right_depth+1;
    }
};
```
