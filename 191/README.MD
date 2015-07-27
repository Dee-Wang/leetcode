# 191 Number of 1 Bits

## Question:

> Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
> 
> For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

求一个unsigned整数的字节中有多少个1，也就是求它的_汉明距离_。

## Solution:

假设整数为m
+ 若二进制串为xxx1,则m-1的二进制串为xxx0,
+ 若二进制串为xx1{n个0},则m-1的二进制串xx0{n个1}，例如11000，10111
无论是哪种情况，将m和m-1相与，都可以将二进制串中的最后一个1变为0.

题目要求个数，只要不停的把最后的1变为0，同时计数，最后整数的二进制串就会全部变为0，也就是说，m=0.

## AC Code:

``` c++
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int result = 0;
	    while(n)
        {
	    	n&=(n-1);
            result++;
        }
        return result;
    }
};
```
