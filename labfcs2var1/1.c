#include <stdio.h>

int
main(void)
{
	int x, i = 0, j;

	if (scanf("%d", &x) != 1) {
		printf("брбрбвыбрббр\n");
		return 1;
	}

	int y[32];

	if (x == 0) {
		printf("0");
		return 0;
	}

	while (x > 0) {
		y[i] = x % 6;
		x /= 6;
		i++;
	}

	for (j = i - 1; j>= 0; j--)
		printf("%d", y[j]);

	printf("\n");

	return 0;
}
