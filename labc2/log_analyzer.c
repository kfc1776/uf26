#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int 
parse_digits(char *s, int n) 
{
	if (n == 2)
		return (s[0] - '0') * 10 + (s[1] - '0');
	else if (n == 4)
		return 	(s[0] - '0') * 1000 +
				(s[1] - '0') * 100 +
				(s[2] - '0') * 10 +
				(s[3] - '0') * 1;
	else
		return -1;
}

int 
leap_year(int year) 
{
    return 
    ((year % 4 == 0) && (year % 100 != 0) || (year % 400));
}

int 
days_in_month(int year, int month) 
{
    int d[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (month < 1 || month > 12) 
		return 0;
    if (month == 2 || leap_year(year)) 
		return 29;

    return d[month - 1];
}

int 
date_time(char *s) 
{
    int digit_pos[] = {0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18}; 

    int year, month, day, hour, minute, second;

    if (strlen(s) != 19) 
		return 0;
    if (s[4] != '-' || s[7] != '-' || s[10] != ' ' || s [13] != ':' || s[16] != ':') 
		return 0;

    for (int i = 0; i < 14; ++i) {
        char ch = s[digit_pos[i]];
        if (!isdigit(ch)) 
			return 0;
    }

    year = parse_digits(s, 4);
    month = parse_digits(s + 5, 2);
    day = parse_digits(s + 8, 2);
    hour = parse_digits(s + 11, 2);
    minute = parse_digits(s + 14, 2);
    second = parse_digits(s + 17, 2);

    if (month < 1 || month > 12)
		return 0;
    if (day < 1 || day > days_in_month(year, month))
		return 0;
    return hour <= 23 && minute <= 59 && second <= 59;
}

int
main(int argc, char *argv[])
{
	FILE *log_in;
	char line[256];

	log_in = fopen(argv[1], "r");

	// TODO проверка открытого файла на NULL
	if (log_in == NULL) {
		perror("холодильник\n");
		return EXIT_FAILURE;
	}
	// ?
	
	// построчное чтение файла
    while (fgets(line, sizeof(line), log_in) != NULL) {
        printf("%s", line);
    }

	fclose(log_in);
	// printf("%s %s %s\n", argv[1], argv[2], argv[3]);
	return 0;
}
