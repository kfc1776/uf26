#include <stdio.h>
#include <stdlib.h>

void
print_array(int *arr, int size)
{
	/*
	 * int i;
	 * for (i = 0; i < size; i++) {
	 * 	printf("%d ", arr[i]);
	 * }
	 * printf("\n");
     */

	for (int *p = arr; p < arr + size; p++)
		printf("%d ", *p);
	
	printf("\n");
}

// max = 1 => ищется max, иначе min
int *
fminmax(int *left, int *right, int max)
{
	if (left == right)
		return NULL;

	int *m = left;

	for (int *c = left; c < right; c++) {
		if ((!max && *c < *m) || (max && *c > *m)) {
			m = c;
		}
	}

	return m;
}

int
sum_between(int *left, int *right)
{
	int *start = (left < right) ? left : right;
	int *end = (left < right) ? right : left;
	int *s, sum = 0;

	for (s = start + 1; s < end; s++)
		sum += *s;

	return sum;
}

void
find_longest_increasing_segment(int *arr, int size, int **start, int **end)
{
	/*
	 * *start = arr;
	 * *end = arr + 1;
	 * int i, max_len = 1;

	 * int current_len, *current_start = arr;

	 * for (i = 1; i < size; i++) {
	 * 	if (arr[i] > arr[i - 1]) {
	 * 		current_len = (&arr[i] - current_start) + 1;
	 * 		if (current_len > max_len) {
	 * 			max_len = current_len;
	 * 			*start = current_start;
	 * 			*end = &arr[i] + 1;
	 * 		}
	 * 	} else {
	 * 		current_start = &arr[i];
	 * 	}
	 * }
	 */

	*start = arr;
	*end = arr + 1;
	int max_len = 1;

	int *current_start = arr;

	for (int *c = arr + 1; c < arr + size; c++) {
		if (*c > *(c - 1)) {
			int current_len = (c - current_start) + 1;
			
			if (current_len > max_len) {
				max_len = current_len;
				*start = current_start;
				*end = c + 1;
			}
		} else {
			current_start = c;
		}
	}
}

void
reverse_segment(int *start, int *end)
{
	int *left = start;
	int *right = end - 1;

	while (left < right) {
		int temp = *left;
		*left = *right;
		*right = temp;

		left++;
		right--;
	}
}

int
main(void)
{
	int n, i;
	scanf("%d", &n);
	int arr[n];
	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	
	int *arr_min = fminmax(arr, &arr[n], 0);
	int *arr_max = fminmax(arr, &arr[n], 1);

	printf("Исходный массив: \n");
	print_array(arr, n);
	printf("\n");

	if (arr_min != NULL && arr_max != NULL) {
		 printf("Минимум: %d\n", *arr_min);
		 printf("Позиция минимума: %ld\n", arr_min - arr);
		 printf("Максимум: %d\n", *arr_max);
		 printf("Позиция максимума: %ld\n", arr_max - arr);
		 printf("Расстояние между минимумом и максимумом: %d\n", abs(arr_max - arr_min));
		 printf("Сумма элементов между минимумом и максимумом: %d\n", sum_between(arr_min, arr_max));
	}
	printf("\n");

	int *segstart = NULL;
	int *segend = NULL;
	find_longest_increasing_segment(arr, n, &segstart, &segend);

	int *ptr;
	printf("Самый длинный возрастающий участок:\n");
	for (ptr = segstart; ptr < segend; ptr++)
		printf("%d ", *ptr);
	printf("\n\n");

	reverse_segment(segstart, segend);
	printf("Массив после разворота выбранного участка:\n");
	print_array(arr, n);

	return 0;
}
