#include <stdio.h>

float
gcd(int a, int b)
{
    if (a == 0)
        return b;

    return gcd(b % a, a);
}

float
pos(float x)
{
	return (x >= 0) ? x : -x;
}

int
main(void)
{
	int a, b;

	if (scanf("%d%d", &a, &b) != 2) {
		printf("2 числа!!!!!!!!!!!!\n");
		return 1;
	}

	printf("НОД: %f, НОК: %f\n", 
			gcd(a, b), 
			pos(a * (b/gcd(a, b)))
			);

	return 0;
}
