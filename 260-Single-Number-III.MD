# 260 Single Number III 

## Question

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.

Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

## Solution 

给出一个数组，其中只有两个数只出现了一次，找出这两个数。

本题主要利用了异或是其本身的反操作的原理，也就是说对同一个数异或两次等于什么也没做。假设a和b是这两个只出现了一次的数

+ 首先用0将数组中所有的数异或一次，即可得到a^b的值，也就得到了a和b中二进制位不同的位
+ 其次用mask = a&(-a),这个操作的作用在于使a^b的二进制位不同的位只剩下一位，从而可以区分a和b,
+ 使用a&masl和b&mask就会则到不同的值，而相同的数n&mask会得到相同的结果
+ 遍历数组中的数，使用n&mask区分a和b，就可以得到a和b中的某一个数
+ 利用先前得到的a^b的值再和第4步中得到的数进行异或，即刻得到另一个数

## AC Code 
```c 
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
	*returnSize = 2;
    int *arr = (int*)malloc(*returnSize * sizeof(int));
    int a = 0, b = 0;
    for (int i = 0; i < numsSize; i++) a ^= nums[i];
    int mask = a&(~(a-1));
    for (int i = 0; i < numsSize; i++) if(nums[i] & mask) b ^= nums[i];
    arr[0] = b;
    arr[1] = a ^ b;
    return arr;
}
```