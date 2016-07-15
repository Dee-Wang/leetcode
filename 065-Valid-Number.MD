# 65 Valid Number

## Queation

Validate if a given string is numeric.

Some examples:

"0" => true  
" 0.1 " => true  
"abc" => false  
"1 a" => false  
"2e10" => true  

## Solution

题目要求检测一个字符串是不是一个有效的数字，但是给出的几个例子太少了，没有完全说清有效数字到底是什么要求，只能一次又一次的试了，导致此题是leetcode上AC率最低的一题，但实际上这题并不难。主要原理就是编译原理中的状态自动机。FSM的表示可以用二位数组，也可以直接用switch case，这里我用了switch case写的更易读一些。最后附上了一些测试案例。

## AC Code

```c
#define S_NORMAL         0
#define S_SIGNED         1
#define S_POINT          2
#define S_INTEGER        3
#define S_FLOAT          4
#define S_ENUMBER        5
#define S_ENUMBER_E      6
#define S_ENUMBER_SIGNED 7
#define S_NUMBER_END     8

#define is_whitespace(c) (c==' ')
#define SIGNED_CASE '+': case '-'
#define DIGIT_CASE                               \
         '0':                                    \
    case '1':                                    \
    case '2':                                    \
    case '3':                                    \
    case '4':                                    \
    case '5':                                    \
    case '6':                                    \
    case '7':                                    \
    case '8':                                    \
    case '9'

bool isNumber(char* s) {
	while(is_whitespace(*s)) {s++;}
	unsigned char state;
    for(state = S_NORMAL; *s; s++) {
        switch(state) {
        case S_NORMAL:
            switch(*s) {
            case '.': state = S_POINT; break;
            case SIGNED_CASE: state = S_SIGNED; break;
            case DIGIT_CASE: state = S_INTEGER; break;
            default: return false;
            }
            break;
        case S_POINT:
	        switch(*s) {
	        case DIGIT_CASE: state = S_FLOAT; break;
	        default: return false;
	        }
	        break;
        case S_SIGNED:
	        switch(*s) {
		    case '.': state = S_POINT; break;
		    case DIGIT_CASE: state = S_INTEGER; break;
		    default: return false;
	        }
	        break;
	    case S_INTEGER:
		    switch(*s) {
		    case DIGIT_CASE: break;
		    case '.': state = S_FLOAT; break;
		    case 'e': state = S_ENUMBER_E; break;
            case ' ': state = S_NUMBER_END; break;
		    default: return false;
	    	}
	    	break;
		case S_FLOAT:
			switch(*s) {
			case 'e': state = S_ENUMBER_E; break;
			case DIGIT_CASE: break;
            case ' ': state = S_NUMBER_END; break;
			default: return false;
			}
			break;
		case S_ENUMBER_E:
			switch(*s){
			case DIGIT_CASE: state = S_ENUMBER; break;
			case SIGNED_CASE: state = S_ENUMBER_SIGNED; break;
			default: return false;
			}
			break;
		case S_ENUMBER:
			switch(*s){
			case DIGIT_CASE: break;
            case ' ': state = S_NUMBER_END; break;
			default: return false;
			}
			break;
		case S_ENUMBER_SIGNED:
			switch(*s){
			case DIGIT_CASE: state = S_ENUMBER; break;
			default: return false;
			}
			break;
		case S_NUMBER_END:
			switch(*s){
			case ' ': break;
			default: return false;
			}
			break;
		default: return false;
    	}
	}
	switch(state){
		case S_INTEGER:
		case S_FLOAT:
		case S_ENUMBER:
	    case S_NUMBER_END:
			return true;
	}
    return false;
}
```

一些测试案例：
```c
int main()
{
	// 以下应为true
    printf("\nresult: %d\n", isNumber("123"));
    printf("\nresult: %d\n", isNumber("1 "));
    printf("\nresult: %d\n", isNumber("1  "));
    printf("\nresult: %d\n", isNumber("+123"));
    printf("\nresult: %d\n", isNumber("-123"));
    printf("\nresult: %d\n", isNumber("3.14"));
    printf("\nresult: %d\n", isNumber("+3.14"));
    printf("\nresult: %d\n", isNumber("-3.14"));
    printf("\nresult: %d\n", isNumber(".14"));
    printf("\nresult: %d\n", isNumber("3."));
    printf("\nresult: %d\n", isNumber("+.14"));
    printf("\nresult: %d\n", isNumber("+3."));
    printf("\nresult: %d\n", isNumber("-.14"));
    printf("\nresult: %d\n", isNumber("-3."));
    printf("\nresult: %d\n", isNumber("2e10"));
    printf("\nresult: %d\n", isNumber("+2e10"));
    printf("\nresult: %d\n", isNumber("-2e10"));
    printf("\nresult: %d\n", isNumber("3.14e10"));
    printf("\nresult: %d\n", isNumber("3.e10"));
    printf("\nresult: %d\n", isNumber("2e+10"));
    printf("\nresult: %d\n", isNumber("2e-10"));
    printf("\nresult: %d\n", isNumber("32.e-80123"));

    // 以下应为false
    printf("\nresult: %d\n", isNumber("."));
    printf("\nresult: %d\n", isNumber("2e+"));
    printf("\nresult: %d\n", isNumber(" "));
    printf("\nresult: %d\n", isNumber("e9"));
    printf("\nresult: %d\n", isNumber("2e"));
    printf("\nresult: %d\n", isNumber(".1."));
    printf("\nresult: %d\n", isNumber(" -."));
    return 0;
}
```