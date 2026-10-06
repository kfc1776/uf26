#include <stdio.h>
#include <stdlib.h>

int
main(void)
{
	int x, y;
	scanf("%d%d", &x, &y);

	printf("%d\n", (x + y + abs(x - y)) / 2);

	return 0;
}
