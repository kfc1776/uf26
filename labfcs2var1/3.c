#include <stdio.h>
#include <stdbool.h>

int
main(void)
{
	int n, m, i;

	if (scanf("%d", &n) != 1) {
		printf("одно число нужно ввести введите пожалуйста ровно одно число иначе программа не будет работать хорошего дня.....\n");
		return 1;
	}

	bool increasing = 1,
		 decreasing = 1;
	
	m = n;
	while (m > 0) {
		if ((m % 10 > (m / 10) % 10) && (m > 10))
			decreasing = 0;
		if ((m % 10 < (m / 10) % 10) && (m > 10))
			increasing = 0;
		m /= 10;
	}

	if (increasing == decreasing) {
		printf("Цифры не упорядочены.\n");
		return 0;
	}

	if (increasing)
		printf("Цифры расположены в порядке возрастания.\n");

	if (decreasing)
		printf("Цифры расположены в порядке убывания.\n");

	return 0;
}
