# 9 Palindrome Number 

## Question:

> Determine whether an integer is a palindrome. Do this without extra space.
> 
> *Some hints:*
> Could negative integers be palindromes? (ie, -1)
> 
> If you are thinking of converting the integer to string, note the restriction of using extra space.
> 
> You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
> 
> There is a more generic way of solving this problem.

## AC Code:
``` c++
class Solution
{
public:
    bool isPalindrome (int x)
    {
        if (x == INT_MIN || x < 0) return false;
        int len = log10 (x) + 1;
        for (int i = 0; i < len / 2; ++i)
        {
            int a = x / (int) pow (10.0, len - i - 1) % 10;
            int b = x / (int) pow (10.0, i) % 10;
            if (a != b) return false;
        }
        return true;
    }
};
```
