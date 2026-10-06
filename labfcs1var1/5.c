#include <stdio.h>

int
main(void)
{
	int m, n;

	scanf("%d%d", &m, &n);

	printf("%d\n", m / 100 + n % 10);
	printf("%d\n", (m / 10) % 10 + n / 100);
	printf("%d\n", m % 10 + (n / 10) % 10);

	return 0;
}
