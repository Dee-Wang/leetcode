# 198 House Robber

## Question:

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
> 
> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

你是一个专业的抢匪，计划去抢了一整条街，但是如果抢了相邻的两个房子，就会引来警察。

给出一个非负的整数列表，代表每个房子里有多少钱，问最多能抢到多少钱？

## Solution:

假设已经抢了第i个房子，那么下一个就不能抢第i+1个，也不能抢第i+4个以后的，因为中间会空出可以抢而没有抢的房间来，只能在i+2和i+3中选择一个钱多的去抢。

## AC Code:
``` python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur = 0, 0
        for i in nums:
            temp = max(pre + i, cur)
            pre, cur = cur, temp
        return cur

```
