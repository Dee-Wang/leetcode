# 38 Count and Say

## Question:

> The count-and-say sequence is the sequence of integers beginning as follows:
> 1, 11, 21, 1211, 111221, ...
> 
> 1 is read off as "one 1" or 11.
> 
> 11 is read off as "two 1s" or 21.
> 
> 21 is read off as "one 2, then one 1" or 1211.
> 
> Given an integer n, generate the nth sequence.
> 
> *Note:* The sequence of integers will be represented as a string.

## AC Code:

``` c++
class Solution
{
public:
    string countAndSay (int n)
    {
        string str = "1";
        for (int i = 1; i < n; ++i)
        {
            str = count (str);
        }
        return str;
    }

    string count (string s)
    {
        string result = "";
        char state = s[0];
        int len = 1;
        for (int i = 1; i < s.length(); ++i)
        {
            if (s[i] == state) len++;
            else
            {
                result += (char) (len + '0');
                result += state;
                state = s[i];
                len = 1;
            }
        }
        result += (char) (len + '0');
        result += state;
        return result;
    }
};
```
