# 28 Implement strStr() 

## Question:

> Implement strStr().
> 
> Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## AC Code:

``` c++
class Solution 
{
public:
    int strStr(char *haystack, char *needle) {
        char *p, *q;
    int len = strlen(haystack) - strlen(needle);

    for (int i = 0; i <= len; i++) {
        p = haystack + i;
        q = needle;
        while (*q && *p == *q) 
        {
            ++p;
            ++q;
        }
        if (*q == 0)
            return i;
    }
    return -1;
    }
};
```
