# 189 Rotate Array

## Question:

> Rotate an array of n elements to the right by k steps.
> 
> For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
> 
> *Note:*
> 
> Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
> 
> *Hint:*
> 
> Could you do it in-place with O(1) extra space?
> 
> Related problem: Reverse Words in a String II

## AC Code:

``` c++
class Solution
{
    public:
    void reverseArray(int *nums, int n)
    {
	    for (int i = 0; i < n/2; ++i)
		    nums[i] ^= nums[n-i-1] ^= nums[i] ^= nums[n-i-1];
    }
    void rotate(int nums[], int n, int k)
    {
        k = k % n;
        reverseArray(nums,n);
        reverseArray(nums,k);
        reverseArray(nums+k,n-k);
    }
};

```
