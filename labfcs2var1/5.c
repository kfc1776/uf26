#include <stdio.h>

int
main(void)
{
	int i;
	for (i = 100; i < 1000; i++)
		if ((i % 10 != (i / 10) % 10) &&
			(i % 10 != i / 100) &&
			(i / 100 != (i / 10) % 10))
			printf("%d ", i);

	printf("\n");

	return 0;
}
