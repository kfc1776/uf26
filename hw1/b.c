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
avg_matrix(int *matrix, int sizeX, int sizeY, int *p)
{
	double sum = 0;
	int *p1, *p2;

	for (p1 = matrix; p1 < matrix + sizeX * sizeY; p1 += sizeY) 
		for (p2 = p1; p2 < p1 + sizeY; p2++)
			sum += (double) (*p2);

	double avg = sum / (double) (sizeX * sizeY);

	for (p1 = matrix; p1 < matrix + sizeX * sizeY; p1 += sizeY)
		for (p2 = p1; p2 < p1 + sizeY; p2++)
			if ((double) (*p2) > avg)
				(*p)++;
	
	return avg;
}

int 
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
	
	return *max;
}

void
replace_maxavg(int *matrix, int sizeY, int maxri, double maxravg)
{
	int trunc_avg = (int)maxravg;

	int *targetrl = matrix + maxri * sizeY; 
	int *targetrr = targetrl + sizeY;       

	int *p;
	for (p = targetrl; p < targetrr; p++) {
		*p = trunc_avg;
	}
}

int
main(void)
{
	int i, j, r, c, counter;

	scanf("%d%d", &r, &c);

	int tmatrix[r][c];

	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
			scanf("%d", &tmatrix[i][j]);

	int rmaxt = 0, cmaxt = 0;
	int biggerthanavg = 0;

	int maxt = findmax(&tmatrix[0][0], r, c, &rmaxt, &cmaxt);
	double avgt = avg_matrix((int*)tmatrix, r, c, &biggerthanavg);

	int maxri = 0;
	double currravg, maxravg = -1e9;

	for (i = 0; i < r; i++) {
		j = 0;
		
		currravg = avg_matrix(&tmatrix[i][0], 1, c, &j);

		if (currravg > maxravg) {
			maxravg = currravg;
			maxri = i;
		}
	}

	printf("Исходная карта:\n");
	print_matrix((int*)tmatrix, r, c);
	printf("Максимальная температура: %d\n", maxt);
	printf("Строка: %d\n", rmaxt);
	printf("Столбец: %d\n", cmaxt);
	printf("Средняя температура карты: %f\n", avgt); 
	printf("Количество значений выше среднего: %d\n", biggerthanavg);
	printf("Строка с максимальным средним: %d\n", maxri);
	printf("Максимальное выбранной строки: %f\n", maxravg);
	
	replace_maxavg((int*)tmatrix, c, maxri, maxravg);
	printf("Карта после замены выбранной строки:\n");
	print_matrix((int*)tmatrix, r, c);

	return 0;
}
