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

int
main(void)
{
	int i, j, r, c;

	scanf("%d%d", &r, &c);

	int tmatrix[r][c];

	for (i = 0; i < r; i++)
		for (j = 0; j < c; j++)
			scanf("%d", &tmatrix[i][j]);

	print_matrix(tmatrix, r, c);

	return 0;
}
