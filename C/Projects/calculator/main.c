#include <stdio.h>



int calculator(int x, int y, char operator) { 
    if (operator == '+') {
        return x + y;
    }
    else if (operator == '-') { 
        return x - y;
    }
    else if (operator == '*' || operator == 'x') {
        return x * y;
    }
    else if (operator == '/') { 
        if (y == 0)  {
            printf("invalid divide number");
            return 0;
        }
        return x / y;
    }

    printf("invalid operation");
    return 0;

}

int main() {
    int x;
    int y;
    char operator;

    printf("enter first num : ");
    scanf("%d", &x);

    printf("enter operation : ");
    scanf(" %c", &operator);

    printf("enter second num : ");
    scanf("%d", &y);



    printf("result : %d", calculator(x, y, operator));

    return 0;
}