#include <stdio.h>
#define bool int
#define true 1
#define false 0
 
int len(int num) {
    int cnt = 0;
    while (num) {
        num /= 10;
        cnt++;
    }   
    return cnt;
}   

int pow(int a, int b) {
    if (b == 0)
        return 1;
    int halfPow = pow(a, b/2);
    return halfPow * halfPow * (b % 2 == 0? 1 : a);
}


int reverse(int num) {
    int ans = 0;
    while (num) {
        ans = ans * 10 + num % 10;
        num /= 10;
    }
    return ans;
}

int giveNthDigit(int num, int digitNum) {
    if (len(num) < digitNum)
        return -1;
    while (digitNum != 1) {
        digitNum--;
        num /= 10;
    }
    return num % 10;
}

int add4(int num) {
    int ans = 0;
    for (int i = 1; i <= len(num); i++)
        ans += pow(10, i - 1) * ((giveNthDigit(num, i) + 14) % 10);
    return ans;
}

int shift(int num) {
    int result = 0;
    for (int i = 1; i < len(num); i++) {
        result += pow(10, i) * giveNthDigit(num, i);
    }
    result += giveNthDigit(num, len(num));
    return result;
}

void input(int *num) {
    *num = 0;
    while ((*num) <= 99999) {
        printf("Please enter an integer greater than 99999: ");
        scanf("%d", num);
        if (*num <= 99999)
            printf("Incorrect input.\n");
    }
    printf("The number entered is %d\n", *num);
}

void printOutput(int encryptNum, int originalNum) {
    printf("Original number: %d\nEncrypted number: %d\n", originalNum, encryptNum);
}

int main() {
    int num;
    input(&num); 
    int test = add4(num);
    //printf("%d\n", test);
    printOutput(shift(add4(num)), num);
    return 0;
}

void input(int *num);
void printOutput(int encryptNum, int originalNum);
