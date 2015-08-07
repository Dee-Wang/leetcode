# 6 ZigZag Conversion

## Question:

> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
> 
> ```
> P   A   H   N
> A P L S I I G
> Y   I   R
> ```
> 
> And then read line by line: ```"PAHNAPLSIIGYIR"```
> 
> Write the code that will take a string and make this conversion given a number of rows:
> 
> ```string convert(string text, int nRows);```
> 
> ```convert("PAYPALISHIRING", 3)``` should return ```"PAHNAPLSIIGYIR".```

## AC Code:

``` c++
class Solution
{
public:
    string convert (string s, int nRows)
    {
		if(nRows==1) return s;
        string strs[nRows];
        int row = 0;
        for (string::iterator it = s.begin(); it != s.end();)
        {
            while (row < nRows && it != s.end()) strs[row++] += *it++;
			row--;
            while (row > 0     && it != s.end()) strs[--row] += *it++;
			row++;
        }
        string result = "";
        for (int i = 0; i < nRows; ++i) result += strs[i];
        return result;
    }
};
```
