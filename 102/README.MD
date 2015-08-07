# 102 Binary Tree Level Order Traversal

## Question:

> Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
> 
> For example:
> 
> Given binary tree ```{3,9,20,#,#,15,7}```,
> ```
>     3
>    / \
>   9  20
>     /  \
>     15   7
> ```
> return its level order traversal as:
> ```
> [
>   [3],
>   [9,20],
>   [15,7]
>   ]
> ```

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
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> >  result;
        if (!root) return result;
        vector<int> current_level;
        queue<TreeNode*> q;
        q.push(root);
        q.push(NULL);
        while(!q.empty()) 
        {
            TreeNode* t = q.front();
            q.pop();
            if (t==NULL) 
            {
                result.push_back(current_level);
                current_level.clear();
                if (q.size() > 0) q.push(NULL);
            } 
            else 
            {
                current_level.push_back(t->val);
                if (t->left) q.push(t->left);
                if (t->right) q.push(t->right);
            }
        }
        return result;
    }
};
```
