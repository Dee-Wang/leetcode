# 111 Minimum Depth of Binary Tree

## Question:

> Given a binary tree, find its minimum depth.
> 
> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

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
    int minDepth(TreeNode *root) {
        if(root==NULL) return 0;
        int min = INT_MAX;
        traversal(root,min,0);
        return min;
    }
    void traversal(TreeNode *root, int& min, int depth)
    {
        if(root->left==NULL&&root->right==NULL)
        {
            if(depth+1<min) min = depth+1;
        }
        if(root->left!=NULL) traversal(root->left,min,depth+1);
        if(root->right!=NULL) traversal(root->right,min,depth+1);
    }
};
```
