#include <stdio.h>
#include <stdlib.h>


int reverse(int x){ 
    int result = 0;

    while (x != 0)
    {
		printf("x is %d\n", x);
        int tail = x % 10;
        int newResult = result * 10 + tail;
		printf("newResult: %d\n tail: %d\n", newResult, tail);
        if ((newResult - tail) / 10 != result)
        { return 0; }
        result = newResult;
        x = x / 10;
    }

    return result;
}

int main(){
	reverse(123321);
	return 0;
}
