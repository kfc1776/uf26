#include <stdio.h>

void
print_matrix(int *matrix, int sizeX, int sizeY)
{
	int *p1, *p2;

	for (p1 = matrix; p1 < matrix + sizeX * sizeY; p1+= sizeY) {
	    for (p2 = p1; p2 < p1 + sizeY; p2++)
			printf("%d ", *p2);
		printf("\n");
	}
	
	printf("\n");
}

double
avg_matrix(int *matrix, int sizeX, int sizeY)
{
	double sum = 0;
	int *p1, *p2;

	for (p1 = matrix; p1 < matrix + sizeX * sizeY; p1 += sizeY) {
		for (p2 = p1; p2 < p1 + sizeY; p2++)
			sum += (double) (*p2);
	}
	
	return sum / (double) (sizeX * sizeY);
}

int *
findmax(int *p, int r, int c, int *pr, int *pc)
{
	int *i, *max = p;
	int imax = 0;

	for (i = p; i < p + r * c; i++) {
		if (*i > *max) {
			max = i;
		}
	}

	*pr = (max - p) / c;
	*pc = (max - p) % c;
	
	return max;
}



int
main(void)
{
	int i, j, r, c;

	scanf("%d%d", &r, &c);

	int tmatrix[r][c];

	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
			scanf("%d", &tmatrix[i][j]);

	int rmaxt = 0, cmaxt = 0;
	int *maxt = findmax(&tmatrix[0][0], r, c, &rmaxt, &cmaxt);

	printf("Исходная карта:\n");
	print_matrix(tmatrix, r, c);
	printf("Максимальная температура: %d\n", *maxt);
	printf("Строка: %d\n", rmaxt);
	printf("Столбец: %d\n", cmaxt);
	printf("Средняя температура карты: %f\n", avg_matrix(tmatrix, r, c)); 

	return 0;
}
