#include <stdio.h>

void inputDate(int *date, int *month, int *year) {
    printf("Please enter a date: ");
    char slashInput;
    scanf("%d%c%d%c%d", date, &slashInput, month, &slashInput, year);
}

void calculateDay(int day, int month, int year) {
    if (month <= 2) {
        year--;
        month += 12;
    }
    int yearOfCentury = year % 100;
    int century = year / 100;
    int R = ((((day + 13 * (month + 1) / 5 + yearOfCentury + yearOfCentury / 4 + century / 4 - 2 * century) % 7 + 7) % 7 + 7) % 7);
    if (month > 12) {
        month -= 12;
        year++;
    }
    printf("The day %d/%d/%d is a ", day, month, year);
    if (R == 0)
        printf("Saturday.\n");
    else if (R == 1)
        printf("Sunday.\n");
    else if (R == 2)
        printf("Monday.\n");
    else if (R == 3)
        printf("Tuesday.\n");
    else if (R == 4)
        printf("Wednesday.\n");
    else if (R == 5)
        printf("Thursday.\n");
    else if (R == 6)
        printf("Friday.\n");
}

int main() {
    int date, month, year;
    inputDate(&date, &month, &year);
    calculateDay(date, month, year);
    return 0;
}

void inputDate(int *date, int *month, int *year);
void calculateDay(int day, int month, int year);
