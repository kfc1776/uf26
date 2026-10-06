#include <stdio.h>

int
main(void)
{
	int op1, op2, op3, res, A, B, C;

	printf("A\tB\tC\tA || B\t!(A || B)\t!(A || B) && C\t(!(A || B) && C) == A\n");

    for (A = 0; A <= 1; A++) {
        for (B = 0; B <= 1; B++) {
            for (C = 0; C <= 1; C++) {
                op1 = A || B;
                op2 = !op1;
                op3 = op2 && C;
                res = (op3 == A);

                printf("%d\t%d\t%d\t%d\t%d\t\t%d\t\t%d\n", A, B, C, op1, op2, op3, res);
            }
        }
    }


	return 0;
}
