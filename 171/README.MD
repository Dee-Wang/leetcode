# 171 Excel Sheet Column Number

## Question:

> Related to question Excel Sheet Column Title
> 
> Given a column title as appear in an Excel sheet, return its corresponding column number.
> 
> For example:
> ```
>     A -> 1
>     B -> 2
>     C -> 3
>     ...
>     Z -> 26
>     AA -> 27
>     AB -> 28
> ```

## Solution:

相当于进制转换，累加就行了。

## AC Code:

``` c++
class Solution {
public:
    int titleToNumber(string s) {
	    int result = 0;
	    for (int i = 0; i < s.length(); i++) 
	    {
		    result *= 26;
	    	result += (s[i]-'A'+1);
	    }
	    return result;
    }
};
```
