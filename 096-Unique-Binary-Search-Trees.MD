# 96 Unique Binary Search Trees

## Question:

> Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
> 
> For example,
> Given n = 3, there are a total of 5 unique BST's.
> 
> ```
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> ```

给定一个数n，使用1..n这n个数能构成多少个平衡二叉树？

## Solution:

假设x作为根结点，那么x的左子树有x-1个结点，x的右子树有n-x个结点。

那么x作为根结点能构成的BST的数量为numTrees(x-1) * numTrees(n-x)。

n个结点能构成的所有BST的数量，就是将这n个结点作为根结点分别构成的BST的数量相加之和。

## AC Code:

``` c++
class Solution {
public:
  int numTrees(int n) {
    int count[n+1] = {0};
    count[0] = 1;
    for(int i = 1; i <= n; ++i) 
      for(int j = 0; j < i; ++j)
        count[i] += count[j] * count[i-j-1];
    return count[n];
  }
};

```
