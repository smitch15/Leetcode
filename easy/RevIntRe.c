int reverse(int x){
	int result = 0;
	while (x > 0){
		int tail = x % 10;
		int newResult = result * 10 + tail;
		if ((newResult - tail) / 10 != result){
			return 0;
		}
		result = newResult;
		x = x / 10;
	}
	return newResult;
}

int main(){
	// check for overflow error with 1123456789
	int x = 123456789;
	printf("reverse func: %d\n", reverse(x));
	return 0;
}
