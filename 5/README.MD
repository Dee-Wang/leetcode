# 5 Longest Palindromic Substring

## Question:

> Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

## AC Code:

``` c++
class Solution {
  public:
    string longestPalindrome(string s) {
        string T;// Transform S to T
        for(int i = 0; i < s.size(); i++)
        { T += "#" + s.substr(i, 1); }
        T.push_back('#');

        vector<int> P(T.size(), 0); // 用数组存储每个起点找到的最长回文子串的长度
        int center = 0, boundary = 0, maxLen = 0, resCenter = 0;
        // center : 右边界对应的中心点
        // boundary : 找到的回文串的最远的右边界，从某个起点开始时，如果这个起点在右边界之内，说明起点到右边界是以前某个回文串的一部分，就可以直接从右边界开始想外扩展。
        // maxLen : 当前找到的回文子串的最大长度
        // resCenter : 当前找到的最大长度的回文子串的中心点，根据中心点和长度可以还原回文串
        for(int i = 1; i < T.size() - 1; i++) {
            int iMirror = 2 * center - i; // calc mirror i = center-(i-center)
            P[i] = (boundary > i) ? min(boundary - i, P[iMirror]) : 0; // shortcut
            while(i - 1 - P[i] >= 0 && i + 1 + P[i] <= T.size() - 1 && T[i + 1 + P[i]] == T[i - 1 - P[i]]) // Attempt to expand palindrome centered at i
            { P[i]++; }
            if(i + P[i] > boundary) { // update center and boundary
                center = i;
                boundary = i + P[i];
            }
            if(P[i] > maxLen) { // update result
                maxLen = P[i];
                resCenter = i;
            }
        }
        return s.substr((resCenter - maxLen) / 2, maxLen);
    }
};
```
