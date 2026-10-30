#include <stdio.h>

int
main(void)
{
	int n, s = 0, i = 1;

	do {
		scanf("%d", &n);
		s += i % 3 != 0 && n % 3 == 0 ? n : 0;
		i++;
	}
	while(n != 0);

	printf("%d\n", s);

	return 0;
}
