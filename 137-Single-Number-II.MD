# 137 Single Number II

## Question:

> Given an array of integers, every element appears three times except for one. Find that single one.
> 
> *Note:*
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

给出一个整数的数组，数组中的每个元素都会出现3次，只有一个除外，要求找出这个数。

注意:

你的算法的时间复杂度应该是线性的，你能否不适用额外的内存空间来实现它。

## Solution:

要想在线性的时间复杂度内完成，我们只能将这个数组遍历一次。

基本原理是，我们可以观察每个元素的二进制串，某个元素出现三次，意味着其相应二进制位上的1也会出现3次。当某个元素第一次出现时，用b来记录相应的二进制串上的1，第二次出现时，用a来记录相应的二进制串上的1，第三次出现时，将a和b相应位置的1清0，表示这个元素已经出现了三次，淘汰。由于只考察二进制串，所以这个元素不必连续出现三次，其他元素的二进制位也可以抵消。

假设给出的数组是[1,1,3,2,3,1,3]，遍历这个数组:

```
// 假设二进制串只有两位，b优先
a = 00, b = 00, 遇到01, a = 00, b = 01
a = 00, b = 01, 遇到01, b 装不了，a来装， a = 01, b = 01
a = 01, b = 01, 遇到11, 1号位的1，b能装，2号位的1都不能装，积满三个，消除，a = 00, b = 10
a = 00, b = 10, 遇到10, a = 10, b = 10
a = 10, b = 10, 遇到11, a = 00, b = 01
a = 00, b = 01, 遇到01, a = 01, b = 01
a = 01, b = 01, 遇到11, a = 00, b = 10
最终b = 10,即2就是Single Number。
```

## AC Code:
``` c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int a = 0, b = 0;
        for(auto i : nums){
            a = b & (a ^ i);
            b = a | (b ^ i);
        }
        
        return b;
    }
};
```
