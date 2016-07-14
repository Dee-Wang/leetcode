# 125 Valid Palindrome

## Question:

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
> 
> For example,
> 
> "A man, a plan, a canal: Panama" is a palindrome.
> "race a car" is not a palindrome.
> 
> *Note:*
> 
> Have you consider that the string might be empty? This is a good question to ask during an interview.
> 
> For the purpose of this problem, we define empty string as valid palindrome.

## AC Code:

``` c++
class Solution
{
public:
    bool isPalindrome (string s)
    {
        eraseInvaildChar (s);
        string::iterator head = s.begin();
        string::iterator tail = s.end() - 1;

        while (head < tail)
        {
            if (*head != *tail) return false;
            head++;
            tail--;
        }

        return true;
    }
private:
    void eraseInvaildChar (string& s)
    {
        for (string::iterator it = s.begin(); it != s.end(); it++)
        {
            *it = toupper (*it);
            if (!isVaildChar (*it)) s.erase (it--);
        }
    }
    bool isVaildChar (char c)
    {
        if (c >= '0' && c <= '9') return true;
        if (c >= 'A' && c <= 'Z') return true;
        return false;
    }
};
```
