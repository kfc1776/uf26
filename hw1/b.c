#include <stdio.h>
#include <stdlib.h>

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
find_max(int *p, int r, int c, int *pr, int *pc)
{
	int *i, *max = p;

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
replace_max_avg(int *matrix, int sizeY, int max_row_i, double max_row_avg)
{
	int trunc_avg = (int)max_row_avg;

	int *target_row_l = matrix + max_row_i * sizeY; 
	int *target_row_r = target_row_l + sizeY;       

	int *p;
	for (p = target_row_l; p < target_row_r; p++) {
		*p = trunc_avg;
	}
}

int
find_max_diff(int *matrix, int sizeX, int sizeY)
{
	int curr_diff, max_diff = 0;
	int *row_l, *row_r;


	for (int i = 0; i < sizeX; i++) {
		row_l = matrix + i * sizeY;
		row_r = row_l + sizeY - 1;

		for (int *c = row_l; c < row_r; c++) {
			curr_diff = abs(*c - *(c + 1));
			if (curr_diff > max_diff) {
				max_diff = curr_diff;
			}
		}
	}
	return max_diff;
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

	int row_max_t = 0, col_max_t = 0;
	int bigger_than_avg = 0;

	int max_t = find_max(&tmatrix[0][0], r, c, &row_max_t, &col_max_t);
	double avg_t = avg_matrix((int*)tmatrix, r, c, &bigger_than_avg);

	int max_row_i = 0;
	double curr_row_avg, max_row_avg = -1e9;

	for (i = 0; i < r; i++) {
		j = 0;
		
		curr_row_avg = avg_matrix(&tmatrix[i][0], 1, c, &j);

		if (curr_row_avg > max_row_avg) {
			max_row_avg = curr_row_avg;
			max_row_i = i;
		}
	}

	printf("Исходная карта:\n");
	print_matrix((int*)tmatrix, r, c);
	printf("Максимальная температура: %d\n", max_t);
	printf("Строка: %d\n", row_max_t);
	printf("Столбец: %d\n", col_max_t);
	printf("Средняя температура карты: %f\n", avg_t); 
	printf("Количество значений выше среднего: %d\n", bigger_than_avg);
	printf("Строка с максимальным средним: %d\n", max_row_i);
	printf("Максимальное выбранной строки: %f\n\n", max_row_avg);
	
	replace_max_avg((int*)tmatrix, c, max_row_i, max_row_avg);
	printf("Карта после замены выбранной строки:\n");
	print_matrix((int*)tmatrix, r, c);

	int max_diff = find_max_diff((int*)tmatrix, r, c);
	printf("Максимальная разница соседних температур: %d\n", max_diff);
	return 0;
}
