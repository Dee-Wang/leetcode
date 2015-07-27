# 226 Invert Binary Tree

## Quedtion:

Invert a binary tree.

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9

```
to
```
     4
   /   \
  7     2
 / \   / \
9   6 3   1

```
> Trivia:
> This problem was inspired by this original tweet by Max Howell:
> Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

## Solution:

翻转二叉树，递归翻转左右子树，再交换左右子树。

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
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return root;
        TreeNode* t = root->left;
        root->left = root->right;
        root->right = t;
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```
