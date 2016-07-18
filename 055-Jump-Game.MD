# 55 Jump Game 

## Question

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

## Solution

给出一个非负整数的数组，初始时你再数组的第一个位置上，其中每个元素代表你最远能跳几个元素，判断是否能到达最后一位。

每次算出最远到多少，判断有没有断层。

## AC Code 
```c 
#define MAX(a,b) a>b?a:b

bool canJump(int* nums, int numsSize) {
    int furthest = 0;
    for(int i = 0; i < numsSize; i++) {
        if(i > furthest) return false;
        furthest = MAX(furthest, i + nums[i]);
    }
    return true;
}
```