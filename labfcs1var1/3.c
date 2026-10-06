#include <stdio.h>

void
printeq(int x1, int x2, int y1, int y2)
{
	int a = y2 - y1;
	int b = x1 - x2;
	int c = x2 * y1 - x1 * y2;

	printf("%dx + %dy + %d = 0\n", a, b, c);
}

int
main(void)
{
	int Ax, Ay, Bx, By, Cx, Cy;
	scanf("%d%d%d%d%d%d", &Ax, &Ay, &Bx, &By, &Cx, &Cy);

	printeq(Ax, Bx, Ay, By);
	printeq(Bx, Cx, By, Cy);
	printeq(Ax, Cx, Ay, Cy);

	return 0;
}
