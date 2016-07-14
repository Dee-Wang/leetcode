# 66 Plus One

## Question:

> Given a non-negative number represented as an array of digits, plus one to the number.
> 
> The digits are stored such that the most significant digit is at the head of the list.

## AC Code:
``` c++
class Solution
{
public:
    vector<int> plusOne (vector<int> &digits)
    {
        int carry = 1;

        for (int i = digits.size() - 1; i >= 0 && carry; --i)
        {
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] %= 10;
        }
        if (carry)
            digits.insert (digits.begin(), 1);
        return digits;
    }
};

```
