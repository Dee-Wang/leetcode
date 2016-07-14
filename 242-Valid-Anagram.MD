# 242 Valid Anagram

## Question:

> Given two strings s and t, write a function to determine if t is an anagram of s.
> 
> For example,
> 
> s = "anagram", t = "nagaram", return true.
> 
> s = "rat", t = "car", return false.
> 
> *Note:*
> 
> You may assume the string contains only lowercase alphabets.

给出两个字符串s和t，判断t是不是s的anagram。

anagram的意思是t是s的字符颠倒顺序得到的。也就是说t和s包含的每种字符的个数一样，但字符的顺序不一样。

## Solution:

两个遍历，计数。

最后判断是否相等。

## AC Code:
``` c++
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> counters(26,0);
        vector<int> countert(26,0);
        for(auto i : s) counters[i -'a']++;
        for(auto i : t) countert[i -'a']++;
        return counters==countert;
    }
};
```
