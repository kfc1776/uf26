#include <stdio.h>

int
main(void)
{
	int n, m, i, j = 0, k;

	if (scanf("%d", &n) != 1) {
		printf("ОДНО число.\n");
		return 1;
	}

	for (i = 1; i < n; i++) 
		j += i;

	m = 1 + j * 2;
	k = m;

	for (i = 1; i < n; i++)
		m += k + 2 * i;

	printf("%d\n", m);

	return 0;
}
