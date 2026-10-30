#include <stdio.h>

int
main(void)
{
	int n, i = 0, t = 1;

	if (scanf("%d", &n) != 1) {
		printf("фффффффффффффф\n");
		return 1;
	}
	
	while (t < n) {
		t += i;
		i++;
	}

	printf("%d\n", t);

	return 0;
}
