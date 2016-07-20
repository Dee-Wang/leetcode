# 238 Product of Array Except Self

## Question

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

## Solution

给出一个整数数组，返回一个数组，使得这个数组中第i位上的数是除了第i位其他所有数字的乘积。

## AC Code 

```c 
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *result = (int*)malloc(numsSize * sizeof(int));
    result[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        result [i] = result[i - 1] * nums[i - 1];
    }
    *returnSize = 1;
    for (int i = numsSize - 1; i >= 0; i--) {
        result[i]   *= (*returnSize);
        *returnSize *= nums[i];
    }
    *returnSize = numsSize;
    return result;
}
```