# Binary Tree Preorder Traversal

## Question:

> Given a binary tree, return the preorder traversal of its nodes' values.
> 
> For example:
> Given binary tree {1,#,2,3},
> 
> ```
>    1
>     \
>      2
>     /
>    3
> 
> ```
> 
> return [1,2,3].

二叉树的先序遍历

## Solution:

二叉树的先序遍历按照根、左、右的顺序进行队规遍历。

不用递归可以用栈来实现。

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret, v1, v2;
        if(root){
            ret.push_back(root->val);
            if(root->left) v1 = preorderTraversal(root->left);
            if(root->right) v2 = preorderTraversal(root->right);
            ret.insert(ret.end(), v1.begin(), v1.end());
            ret.insert(ret.end(), v2.begin(), v2.end());
        }
        return ret;
    }
;
```

