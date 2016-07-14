# 35 Search Insert Position

## Question:

> Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
> 
> You may assume no duplicates in the array.
> 
> Here are few examples.
> 
> ```
> [1,3,5,6], 5 → 2
> [1,3,5,6], 2 → 1
> [1,3,5,6], 7 → 4
> [1,3,5,6], 0 → 0
> ```

## Solution:

二分查找

## AC Code:

``` c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int start=0, end=nums.size()-1, mid;
        while(start<=end){
            mid = (end+start)/2;
            if(nums[mid]<target){
                mid++;
                start = mid;
            }
            else if(nums[mid] > target) end = mid-1;
            else return mid;
        }
        return mid;
    }
};
```
