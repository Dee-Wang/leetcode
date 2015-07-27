# 94 Binary Tree Inorder Traversal

## Question:

> Given a binary tree, return the inorder traversal of its nodes' values.
> 
> For example:
> Given binary tree {1,#,2,3},
> ```
>    1
>     \
>      2
>     /
>    3
> 
> ```
> return [1,3,2].
> 
> Note: Recursive solution is trivial, could you do it iteratively?

中序遍历二叉树。

## Solution:

一般遍历二叉树都会想到递归，若不用递归，可以用栈来辅助迭代。这次试试Morris Traversal算法。

根据线索二叉树的概念，利用叶子的左右空闲指针指向遍历的前驱或后继节点。

+ 初始化当前节点为cur
+ 若cur不为空
  - 若当前节点没有左孩子，则访问当前节点，并将当前节点右移
  - 若当前节点有做孩子，则找到左子树最右边的节点（也就是中序遍历的最后一个节点）:
    + 若它的右指针为空，就指向cur，并将当前节点左移
    + 若它的右指针不为空，表明这颗子树已经遍历完了，将右指针重新赋为空，访问当前节点，将当前节点右移
+ 循环第二步

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
    vector<int> inorderTraversal(TreeNode* root) {
        TreeNode *cur = root;
        vector<int> ret;
        while(cur){
            if(cur->left){
                TreeNode *precur = cur->left;
                while(precur->right && precur->right != cur) precur = precur->right;
                if(precur->right){
                    precur->right = NULL;
                    ret.push_back(cur->val);
                    cur = cur->right;
                }else{
                    precur->right = cur;
                    cur = cur->left;
                }
            }else{
                ret.push_back(cur->val);
                cur = cur->right;
            }
        }
        return ret;
    }
};
```
