#include <stdio.h>


int pow(int num1, int powtime) {
    int result = 1;
    for (int i = 0; i < powtime; i++) {
        result = result * num1;
    } 
    return result;

} 


int main() {

    int base_type = 0;
    int base = 0;
    int base_list[12];
    
    

   printf("enter ur ur number : ");
   scanf("%d", &base);
   printf("enter ur base type : ");
   scanf("%d", &base_type);


   if (base_type == 2 || base_type == 10) {
        int size = 0;
        size_t size_of_base = sizeof(base);
        
        while (base > 0) {
            base_list[size++] = base % 10;
            base /= 10;
        } 
        
        int result = 0;
        int placement = 0;

        for (int i = size - 1; i >= 0; i--) {
            result = result + base_list[i] * pow(base_type, i);
        } 

        printf("%d", result);
   }else {
        printf("we do not support that form of base yet");
   } 

    return 0;
} 