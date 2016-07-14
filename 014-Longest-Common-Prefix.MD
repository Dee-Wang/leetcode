# 14 Longest Common Prefix 

## Question:

> Write a function to find the longest common prefix string amongst an array of strings.

## AC Code:

``` c++
class Solution
{
public:
    string longestCommonPrefix (vector<string> &strs)
    {
        string prefix = "";
        if (strs.empty()) return prefix;
		if(strs.size() == 1) return strs[0];
        int max_len = 0;
        for (int i = 0; i < strs.size(); ++i)
        {
            if (strs[i].length() >= max_len)
            {
                max_len = strs[i].length();
                prefix = strs[i];
            }
        }
        for (int i = 0; i < strs.size(); ++i)
        {
            prefix = getCommomPrefix (strs[i], prefix);
            if (prefix.length() == 0) return prefix;
        }
		return prefix;
    }

    string getCommomPrefix (string a, string prefix)
    {
        string result = "";

        for (int i = 0; i < prefix.length(); i++)
        {
            if (a[i] == prefix[i]) result += a[i];
            else break;
        }

        return result;
    }
};
```
