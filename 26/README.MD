# 26 Remove Duplicates from Sorted Array 

## Question:

> Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
> 
> Do not allocate extra space for another array, you must do this in place with constant memory.
> 
> For example,
> Given input array nums = ```[1,1,2]```,
> 
> Your function should return length = ```2```, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

## AC Code:

``` c++
class Solution
{
public:
    int removeDuplicates (int A[], int n)
    {
		if(n == 0) return 0;
        int pos = 0;
        for (int i = 1; i < n; ++i)
        {
            if (A[i] != A[pos])
            {
                A[++pos] = A[i];
            }
        }
        return pos + 1;
    }
};
```
