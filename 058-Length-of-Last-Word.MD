# 58 Length of Last Word 

## Question:

> Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
> 
> If the last word does not exist, return 0.
> 
> *Note:* A word is defined as a character sequence consists of non-space characters only.
> 
> For example, 
> 
> Given s = "Hello World",
> 
> return 5.

## AC Code:

``` c++
class Solution
{
public:
    int lengthOfLastWord (const char *s)
    {
        int len = 0;
        char *p = (char*) s;
        int state = 0;
        while (*p)
        {
            if (*p == ' ')
            {
                state = 0;
            }
            else
            {
                if (state == 0)
                {
                    state = 1;
                    len = 1;
                }
                else
                    len++;
            }
            p++;
        }
        return len;
    }
};
```
