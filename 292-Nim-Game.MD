# 292 Num Game  

## Question

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

## Solution

Nim Game 就是有一堆石头，两个人轮流拿石头，一次可以拿1个，2个或者3个，谁拿到最后一个谁就输了。

题目要就输入石头的数量，判断你是否能赢，你后拿。

## AC Code 
```c 
bool canWinNim(int n) {
    return n % 4;
}
```