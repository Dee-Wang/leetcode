# 338 Counting Bits

## Question

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

## Solution

给出一个非负整数num，对于 [0, num] 之间的每个整数，算出其二进制上有多少位1。然后返回一个数组。

2^(n-1) 到 2^n 总比 2^(n-2) 到 2^(n-1) 的最高位多一个1.

## AC Code  

```c
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    *returnSize = num + 1;
    int *arr = (int*)malloc(*returnSize * sizeof(int));
    arr[0] = 0;
    arr[1] = 1;
    int offset = 2;
    for(int i = 2; i <= num; i++){
	    if(i == offset * 2) offset = i;
	    arr[i] = arr[i - offset] + 1;
    }
    return arr;
}
```