# 20 Valid Parentheses

## Question:

> Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
> 
> The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## AC Code:

``` c++
class Solution
{
public:
    bool isValid (string s)
    {
        stack<char> stk;
        for (int i = 0; i < s.length(); ++i)
        {
            switch (s[i])
            {
            case '(':
                stk.push (')');
                break;
            case '[':
                stk.push (']');
                break;
            case '{':
                stk.push ('}');
                break;
            case ')':
            case ']':
            case '}':
				if(stk.empty()) return false;
                if (stk.top() != s[i]) return false;
                stk.pop();
                break;
            default:
                break;
            }
        }
		if(stk.empty()) return true;
		else return false;
    }
};
```
