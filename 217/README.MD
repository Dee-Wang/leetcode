# 217 Contains Duplicate 

## Question:

> Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

## Solution:

给定一个数组，如果数组中有相同的数就返回true, 否则就返回false.

遍历，回溯查找

## AC Code:

``` c++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uset;
        for(auto it = nums.begin(); it != nums.end(); ++it){
            if(uset.find(*it) != uset.end()) return true;
            else uset.insert(*it);
        }
        return false;
    }
};
```
