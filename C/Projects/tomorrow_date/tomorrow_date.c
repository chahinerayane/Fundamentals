#include <stdio.h>
#include <stdlib.h>

typedef enum {
    JANUARY = 1, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER , NOVEMBER , DECEMBER 
}day;

int is_leap(int y) {
    if ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0)) {
        return 1;
    }
    return 0;
}


int main() {

    int d = 0,m = 0,y = 0, max_days = 0;;

    printf("Enter day/month/year in same format : ");
    
    if (scanf("%d/%d/%d", &d, &m, &y) != 3) {
        printf("Invalid format !");
        return -1;
    }

    

    switch (m)
    {
        case JANUARY:
        case MARCH:
        case MAY:
        case JULY:
        case AUGUST:
        case OCTOBER:
        case DECEMBER:

        max_days = 31;

        if (d > max_days || d < 1) {
            printf("Invalid date");
            return -1;
        }

        if ( d < max_days) {
            d += 1;
        }else {
            d = 1;
            if (m < DECEMBER) {
                m += 1;
            }else {
                m = JANUARY;
                y += 1; 

            }
        }

        break;

        case APRIL:
        case JUNE:
        case SEPTEMBER:
        case NOVEMBER:

            max_days = 30;

            if (d > max_days || d < 1) {
                printf("Invalid date");
                return -1;
            }


            if (d < 30) {
                d += 1;
            }else {
                d = 1;
                m += 1;
            }
            break;
        case FEBRUARY : 

            if (is_leap(y)) {
                max_days = 29;
            }
            else {
                max_days = 28;
            }

            if (d > max_days || d < 1) {
                printf("Invalid date");
                return -1;
            }

            if (d < max_days) {
                d += 1;
            }else {
                d = 1;
                m += 1;
            }
            
            break;

    default:
        printf("Invalid date");
        return -1;
    }

    printf("%02d/%02d/%02d", d, m, y);

    return 0;
}