# 371 Sum of Two Integers 

## Question

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

## Solution

计算两个数之和，但不能用+或者-。

用循环++和--也可以，但没什么意思。现在尝试用位运算来解决。

由于用位运算来操作操作的是二进制数据，只要能把a和b的二进制位用逢二进一的二进制加法加起来就可以了。

+ 用`a&b`判断a和b的二进制加法中是否存在均为1的情况，即是否存在进位。
+ 如果存在则把`a&b`左移一位，即可得到进位
+ 用`a^b`可以得到a和b的二进制加法中一位为0，一位为1的情况，即无需进位的结果。
+ 然后递归将进位和无需进位的结果加起来
+ 当不存在进位的情况时，直接使用`a|b`将进行二进制加法得到结果，返回递归

整个过程实际上就是模拟了逢二进一的二进制加法。

## AC Code
```c 
int getSum(int a, int b) {
    return a & b ? getSum((a & b) << 1, a ^ b) : a | b;
}
```
