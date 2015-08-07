# 172 Factorial Trailing Zeroes

## Question:

> Given an integer n, return the number of trailing zeroes in n!.
> 
> *Note:* Your solution should be in logarithmic time complexity.

## AC Code:

``` c++
class Solution {
public:
    int trailingZeroes(int n) {
        int result = 0;
		while(n)
		{
			result += (n/5);
			n/=5;
		}
		return result;
    }
};
```
