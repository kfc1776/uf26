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

int *
findmax(int *p, int r, int c)
{
	int i, max = *p;
	
	for (i = 0; i < r * c; i++) 
		if (*(p + i) > max)
			max = *(p + i);

	return max;
}

//

int
main(void)
{
	int i, j, r, c;

	scanf("%d%d", &r, &c);

	int tmatrix[r][c];

	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
			scanf("%d", &tmatrix[i][j]);

	printf("Исходная карта:\n");
	print_matrix(tmatrix, r, c);
	printf("Максимальная температура: %d\n", findmax(&tmatrix[0][0], r, c));

	return 0;
}
