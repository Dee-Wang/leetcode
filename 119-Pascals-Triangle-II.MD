# 119 Pascal's Triangle II 

## Question:

> Given an index k, return the kth row of the Pascal's triangle.
> 
> For example, given k = 3,
> 
> Return [1,3,3,1].
> 
> *Note:*
> 
> Could you optimize your algorithm to use only O(k) extra space?

## AC Code:

``` c++
class Solution
{
public:
    vector<int> getRow (int rowIndex)
    {
        vector<int> result;
        for (int i = 0; i < rowIndex + 2; ++i)
        {
            int temp = 1;
            for (int j = 1; j < i - 1; ++j)
            {
                int temp2 = result[j];
                result[j] += temp;
				temp = temp2;
            }
            if(i <rowIndex+1) result.push_back (1);
        }
        return result;
    }
};

```
