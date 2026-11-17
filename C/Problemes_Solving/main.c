#include <stdio.h>
#include <math.h>


void update(int *a,int *b) {
    int ap = *a + *b;
    int bp = abs(*a - *b);
    *a = ap;
    *b = bp;
    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
