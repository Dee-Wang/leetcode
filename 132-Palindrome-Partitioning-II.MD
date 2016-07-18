# 132 Palindrome Partitioning II

## Question

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",

Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

## Solution

给出一个字符串，将这个字符串分隔成多个子串，且每个子串都是回文串，返回最少的分隔次数。

例如，s = "aab"，可以分割成["aa", "b"]两个回文串，最少只需一次分割，所以返回1。

使用一个数组cut来记录回文串的分组，一个字符串做多可以分为每个字符一组，也就是n组(n为字符串长度)。初始化cut为1...n。

遍历每个字符作为中心，然后偏移量offset逐渐增加，判断中心两侧offset的字符是否相等，来判断是否回文。

这里注意回文有两种，一种形如"abcba"的奇数串，一种形如"abba"的偶数串，要分别处理。

动态更新cut数组，使得cut数组对应回文串的最高位(更新后的分组)为最低位(更新前的分组)+1和其本身的较小值。

最终可推导出最后一个分组，最后一个分组的组别号-1就是分割次数。


## AC Code 
```c 
#define MIN(a,b) a<b?a:b

int minCut(char *s) {
    int len = strlen(s);
    int cut[len + 1];
    for(int i = 0; i <= len; i++) cut[i] = i;
    for(int center = 0; center < len; center++) {
        for(int offset = 0; center - offset >= 0 && center + offset < len
              && s[center - offset] == s[center + offset]; offset++)
            cut[center + offset + 1] = MIN(cut[center + offset + 1], cut[center - offset] + 1);
        for(int offset = 0; center - offset - 1 >= 0 && center + offset < len
              && s[center - offset - 1] == s[center + offset]; offset++)
            cut[center + offset + 1] = MIN(cut[center + offset + 1], cut[center - offset - 1] + 1);
    }
    return cut[len] - 1;
}
```