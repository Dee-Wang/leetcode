# 190 Reverse Bits

## Question:

> Reverse bits of a given 32 bits unsigned integer.
> 
> For example, given input 43261596 (represented in binary as *00000010100101000001111010011100*), return 964176192 (represented in binary as *00111001011110000010100101000000*).
> 
> *Follow up:*
> 
> If this function is called many times, how would you optimize it?

## AC Code:

``` c++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int ret = 0, leftshift = 31;
        while(n)
        {
            int t = n&0x01; //取得n的二进制串的最后一位
            t <<= leftshift; //将取得的二进制数左移到相应位置
           ret |= t; //将取得的数在相应位置上赋值给ret
           leftshift--;
           n >>= 1; //右移一次，挤掉最后一位
        }
        return ret;
    }
};
```
