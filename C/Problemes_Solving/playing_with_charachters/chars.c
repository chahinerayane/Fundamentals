#include <stdio.h>

int main() {
    char ch;
    char s[25];
    char sen[100];   

    scanf("%c", &ch);
    scanf("%24s", s);
    scanf(" %99[^\n]", sen); 
    
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen); 
    
    return 0;
}
