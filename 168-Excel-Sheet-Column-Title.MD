# 168 Excel Sheet Column Title

## Question:

> Given a positive integer, return its corresponding column title as appear in an Excel sheet.
> 
> For example:
> 
> ```
>     1 -> A
>     2 -> B
>     3 -> C
>     ...
>     26 -> Z
>     27 -> AA
>     28 -> AB
> ```

## AC Code:

``` c++
class Solution {
public:
    string convertToTitle(int n) {
        string result = "";
        n--;
        while(n>=0)
        {
	        result += (char)(n%26+'A');
	        n = n/26-1;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```
