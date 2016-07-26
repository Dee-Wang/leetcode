# 347 Top K Frequent Elements

## Question

Given a non-empty array of integers, return the k most frequent elements.

For example,

Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
- You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
- Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Solution

给出一个非空的整数数组，返回出现次数最多的k个元素。

hash表计数，然后排序，输出前k个。

## AC Code 
```c 

struct nc_t {
    int number;
    int count;
    UT_hash_handle hh;
};

int comp(struct nc_t *a, struct nc_t *b)
{
    return (b->count - a->count);
}

int* topKFrequent(int* nums, int numsSize, int k, int* returnSize) {
    struct nc_t *counters = NULL;
    int *result, i, j, len = 0;

    result = (int *)malloc(sizeof(int) * numsSize);

    for(i = 0; i < numsSize; i++) {
        struct nc_t *find = NULL;
        HASH_FIND_INT(counters, nums + i, find);
        if(find == NULL) {
            struct nc_t *x = malloc(sizeof(struct nc_t));
            x->number = nums[i];
            x->count = 1;
            HASH_ADD_INT(counters, number, x);
            len ++;
        } else {
            find->count++;
        }
    }

    HASH_SORT(counters, comp);

    struct nc_t *iter = counters;
    for(i = 0; i < k; i++) {
        printf("(%d, %d)\n", iter->number, iter->count);
        result[i] = iter->number;
        iter = iter->hh.next;
    }

    HASH_CLEAR(hh, counters);
    *returnSize = k;
    return result;
}
```