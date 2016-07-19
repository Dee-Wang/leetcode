# 283 Move Zeros

## Question
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

## Solution

给出一个数组，把数组中所有的0移动到数组的尾部，并保持非0元素的顺序。

## AC Code


```c
void swapint(int *a, int *b) {
    int c;
    c = *a;
    *a = *b;
    *b = c;
}

void moveZeroes(int* nums, int numsSize) {
    int index = 0;
    for (int i = 0; i < numsSize; i++) {
	if(nums[i] != 0) swapint(&nums[index++], &nums[i]);
    }
}
```
