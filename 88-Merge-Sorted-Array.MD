# 88 Merge Sorted Array

## Question:

> Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
> 
> *Note:*
> 
> You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

## AC Code:

``` c++
class Solution
{
public:
    void merge (int A[], int m, int B[], int n)
    {
        memmove (A + n, A, m * sizeof (int));
        int ia = n, ib = 0, ic = 0;
        while (ia < m + n || ib < n)
        {
            int a = ia < m + n ? A[ia] : INT_MAX;
            int b = ib < n ? B[ib] : INT_MAX;
            if (a >= b)
            {
                a = b;
                ib++;
            }
            else
                ia++;
            A[ic++] = a;
        }
    }
};

```
