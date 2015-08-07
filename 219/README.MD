# Contains Duplicate II

## Question:

> Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

给出一个整形数组，找出第i个数和第j个数之间是否有相同的数，有则返回true，否则返回false，i和j的最大差距是k。

## Solution:

用一个vector的前k+1个数构造一个unordered_set容器，若容器的size()小于k+1，说明前k+1个数中有重复的数在构造中直接剔除了，返回false。

从第k+2个数开始遍历，每次删除前一个数，加入后一个数，再判断是否重复。

## AC Code:

``` c++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
		int size = nums.size();
		int maxCount = k+1;
		if(size <= maxCount ){
			unordered_set<int> uset(nums.begin(), nums.end());
			return uset.size() != size;
	    }

		unordered_set<int> uset(nums.begin(), nums.begin()+maxCount);
		for(auto it = nums.begin()+maxCount; it != nums.end(); ++it){
			if( uset.size() != maxCount ) return true;
			uset.erase(*(it-maxCount));
			uset.insert(*it);
		}
		return uset.size() != maxCount;
	}
};
```
