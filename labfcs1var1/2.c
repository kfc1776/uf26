#include <stdio.h>
#include <math.h>

int
main(void)
{
	int x, i, t;
	scanf("%d", &x);
	
	for (i = 1; i < 7; i++) {
		t = (int)(x / pow(10, 6 - i)) % 10;
		printf("%d", t % 2);
	}

	printf("\n");

	return 0;
}
