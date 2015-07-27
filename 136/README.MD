# 136 Single Number

## Question:

> Given an array of integers, every element appears twice except for one. Find that single one.
> 
> Note:
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给出一个整形的数组，数组每个元素都会出现两次，只有一个元素只出现一次，找出这个元素。

## Solution:

用0对数组中的所有元素进行异或，出现两次的元素会异或两次，这两次异或的效果会抵消，而出现一次的元素与0异或得到的就是single number.

灵感来自于[一道逻辑题 - 我拿走了哪个数](http://www.cnblogs.com/baiyanhuang/archive/2010/06/23/1763981.html)

## AC Code:

``` c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ret = 0;
        for(int i = 0; i< nums.size(); ++i) ret ^= nums[i];
        return ret;
    }
};
```
