#include <stdio.h>
#include <string.h>

int
main(void)
{
	char mask[8];
	int x, i, s = 0;
	int mda[8], xda[8];

	scanf("%d%s", &x, &mask);
	
	for (i = 0; i < 8; i++) {
		mda[i] = (int)mask[i] - (int)'0';
		xda[7-i] = x % 10;
		x /= 10;
	}

	for (i = 0; i < 8; i++)
		s += xda[i] * mda[i];

	printf("%d\n", s);

	return 0;
}
