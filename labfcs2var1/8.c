#include <stdio.h>
#include <stdbool.h>

int
main(void)
{
	int n, i, j;
	bool f = 0;

	if(scanf("%d", &n) != 1 || n < 1) {
		printf("неправильно.\n");
		return 1;
	}

    for (i = 1; i * i < n; i++) {
        for (j = i; i * i + j * j <= n; j++) {
            if (i * i + j * j == n) {
                printf("%d = %d^2 + %d^2 (%d + %d)\n",
						N, a, b, a * a, b * b);
                f = 1;
            }
        }
    }	

	if (!f)
		printf("https://gcc.gnu.org/pipermail/gcc-rust/2024-May/001735.html\n");

	return 0;
}
