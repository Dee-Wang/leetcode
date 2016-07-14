# 155 Min Stack

## Question:

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
> 
> push(x) -- Push element x onto stack.
> 
> pop() -- Removes the element on top of the stack.
> 
> top() -- Get the top element.
> 
> getMin() -- Retrieve the minimum element in the stack.

## AC Code:

``` c++
class MinStack
{
    public:
        stack<int> stk;
        stack<int> min;

        void push(int x)
        {
            // If empty
            if(min.empty())
            {
                stk.push(x);
                min.push(x);
                return;
            }

            // Not empty
            stk.push(x);

            if(x <= min.top())
                min.push(x);
        }

        void pop()
        {
            if(!min.empty())
            {
                if(stk.top() == min.top())
                    min.pop();
                stk.pop();
            }
        }

        int top()
        {
            return stk.top();
        }

        int getMin()
        {
            return min.top();
        }
};
```
