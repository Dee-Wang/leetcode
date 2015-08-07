# 3 Longest Substring Without Repeating Characters

## Question:

> Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

## AC Code:

``` c++
class Solution {
public:
  int lengthOfLongestSubstring(string s) { 
    string str;
	int max_len = 0;
	for (int i = 0; i < s.size(); i++) {
	  int pos = str.find(s[i]);
	  if(pos != string::npos){
		max_len = max(max_len, (int)str.size());
	    str = str.substr(pos+1,s.size()-pos-1);
	  }
	  str += s[i];
	}
	return max(max_len,(int)str.size());
  }
};

```
