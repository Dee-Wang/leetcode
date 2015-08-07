# 70 Climbing Stairs

## Question:

> You are climbing a stair case. It takes n steps to reach to the top.
> 
> Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## AC Code:

``` c++
class Solution
{
public:
    int climbStairs (int n)
    {
        int a = 1, b = 0, result = 0;
        for (int i = 0; i < n; i++)
        {
            result = a + b;
            b = a;
            a = result;
        }
        return result;
    }
};

```
