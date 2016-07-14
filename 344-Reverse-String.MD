# 344 Reverse String

## Question

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

翻转输入的字符串


## AC Code
```c
// 交换像个指针指向的字符
void swap(char *a, char *b) {
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

char* reverseString(char* s) {
    int len = strlen(s);
    char *b = s, *e = s + len - 1;
    while(b < e) {
        swap(b,e);
        b++, e--;
    }
    return s;
}
```