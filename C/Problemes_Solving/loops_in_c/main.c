#include <stdio.h>
#include <string.h>

int main() {

    const char *nums[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    int a, b;
    scanf("%d\n%d", &a, &b);

    for (int i = a; i <= b; i++)
    {
        if (i >= 1 && i <= 9) {
            printf("%s\n", nums[i]);
        }
        else {
            if (i % 2 == 0) {
                printf("even\n");
            }else {
                printf("odd\n");
            }
        }
    }
    
    return 0;
}