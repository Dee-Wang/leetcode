# 169 Majority Element

## Question:

> Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
> 
> You may assume that the array is non-empty and the majority element always exist in the array.

## AC Code:
``` c++
class Solution {
public:
    int majorityElement(vector<int> &num) {
        int majority_element = num[0];
        int count = 0;
        for (vector<int>::iterator iter = num.begin(); iter != num.end(); iter++) 
        {
        	if(*iter == majority_element) count++;
        	else if(count == 0) majority_element = *iter;
        	else count--;
        }
        return majority_element;
    }
};
```
