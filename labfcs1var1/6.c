#include <stdio.h>

int
main(void)
{
	int n;
	scanf("%d", &n);
	printf("%d\n", n / 100 + n % 100);
	return 0;
}
