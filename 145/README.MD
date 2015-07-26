# 145 Binary Tree Postorder Traversal

## Question:

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
```
   1
    \
     2
    /
   3

```
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

后序遍历二叉树。

## Solution:

后序遍历可以先根据根、右、左的顺序遍历，然后将结果倒转过来。

注意栈的特点，push时先左后右。

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        stack<TreeNode*> stk;
        
        if(root == NULL) return ret;
        
        stk.push(root);
        while(!stk.empty()){
            TreeNode *p = stk.top();
            stk.pop();
            ret.push_back(p->val);
            if(p->left) stk.push(p->left);
            if(p->right) stk.push(p->right);
        }
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```
