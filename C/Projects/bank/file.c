#include <stdio.h>


void write() {
    FILE * pFile = fopen("users.txt", "w");

    char text[] = "User 1 name is name";

    if (pFile == NULL) {
        printf("Error oppenning file !");
    }

    fprintf(pFile, "%s", text);

    printf("File was written successfully");

    fclose(pFile);
}


int main() {

    FILE * pFile = fopen("users.txt", "r");

    char buffer[1024] = {0};

    if (pFile == NULL) {
        printf("Error oppenning file !");
        return -1;
    }

    while (fgets(buffer, sizeof(buffer), pFile) != NULL)
    {
        printf("%s", buffer);
    }
    

    fclose(pFile);

}