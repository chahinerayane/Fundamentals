#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct
{
    char name[50];
    int age;
    float balance;

}Bank;


void cleaner() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

bool age_checker(int age) {
    return age >= 18;
}

bool is_valid_amount(float amount) {
    return amount > 0;
}

bool File_writer(char name[50], int age, float balance) {

    FILE * pFile = fopen("users.txt", "w");

    if (pFile == NULL) {
        return false;
    }

    fprintf(pFile, "%s ", name);
    fprintf(pFile, "%d ", age);
    fprintf(pFile, "%.2f ", balance);

    fclose(pFile);

    return true;

}

Bank * create_account(Bank * t) {
    
    char name[50] = {0};
    int age = 0;
    float amount = 0.0f;

    printf("Enter you're name : ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';

    printf("Enter you're age : ");
    scanf("%d", &age);

    if (!age_checker(age)) {
        printf("You are not able to create an account under age");
        exit(EXIT_FAILURE);
    }

    printf("Enter the amount you want to deposit : ");
    scanf("%f", &amount);

    if(!is_valid_amount(amount)) {
        printf("You are not able to create an account under age");
        exit(EXIT_FAILURE);
    }
    
    strcpy(t->name, name);
    t->age = age;
    t->balance = amount;

    if (File_writer(t->name, t->age, t->balance) == false) {
        exit(EXIT_FAILURE);
        
    }

    printf("account seccssufully created");

    return t;

}




Bank * show_info(Bank * t) {
    return t;
}


Bank * update(Bank * t) {
    

    int choice = 0;
    char options[3][50] = {"name", "age", "back"};
    char new_name[50];
    int new_age = 0;
    bool is_changing = true;
   

    while (is_changing)
    {   
        printf("\n\n");

        for (int i = 0; i < sizeof(options) / sizeof(options[0]); i++) {
            printf("%d . %s\n", i + 1, options[i]);
        }

        printf("\n\n  Enter the option u want to change : ");

        if (scanf("%d", &choice) != 1) {
            printf("Taking user input Failed !\n\n");
            cleaner();
            continue;
        }else {
            getchar();

            switch (choice)
            {
                case 1:
                    printf("\n\nEnter ur new name : ");

                    if (fgets(new_name, sizeof(new_name), stdin) == NULL || strlen(new_name) == 1) {
                        printf("Something went wrong !");
                        cleaner();
                        continue;
                    }

                    else {
                        new_name[strcspn(new_name, "\n")] = '\0'; 

                        strncpy(t->name, new_name, sizeof(t->name) - 1); 

                        t->name[sizeof(t->name) - 1] = '\0'; 
                    }
        
                    break;

                case 2:
                    
                    printf("Enter ur new age : ");
                    if (scanf("%d", &new_age) != 1) {
                        printf("Taking user input Failed !");
                        cleaner();
                        continue;
                    }else {
                        if (age_checker(new_age)) {
                            t->age = new_age;
                        }else {
                            printf("Invalid age or not old enought !");
                        }
                    }

                    
                    break;

                case 3 :
                    is_changing = false;
                    break;
                
                default:
                    printf("Invalid choice !");
                    break;
            }
        
        }

    }
    
    return t;

}

Bank * withdraw(Bank * t) {

    float amount = 0.0f;

    printf("\n\nEnter the amount of money u want to withdraw : ");

    if (scanf("%f", &amount) != 1 || !(is_valid_amount(amount))) {
        printf("Taking user input Failed !\n");
        cleaner();
    }else {

        if (t->balance >= amount) {
            t->balance -= amount;
            printf("U just withdrawed : %.2f", amount);
        }
        else {
            printf("You do not have enought cash !");
        }


    }

    
    
    return t;
}

Bank * deposit(Bank * t) {

    float amount = 0.0f;

    printf("\n\nEnter the amount of money u want to add : ");

    if (scanf("%f", &amount) != 1 || !(is_valid_amount(amount))) {
        printf("Taking user input Failed !\n");
        cleaner();
    }else {
        t->balance += amount;
    }

    
    
    return t;
}

int main() {

    Bank user1 = {"John", 20, 500.00};
    Bank * pUser;

    bool is_Running = true;
    int choice = 0;
    
    char options[6][50] = {"Show info", "show balance", "edit", "deposit", "withdraw", "exit" };

    while (is_Running) {

        printf("\n\nWelcome to the C system bank :)\n\n");

        for (int i = 0; i < sizeof(options) / sizeof(options[0]); i++) {
            printf("%d . %s\n", i + 1, options[i]);
        }   

        printf("\n    => Enter ur choice : ");
        
        if (scanf("%d", &choice) != 1) {
            printf("Taking user input failed !");
            cleaner();
            return 1;
        }

        switch (choice)
        {
            
        case 1 :
        case 2 :

            printf("\n\n");

            pUser = show_info(&user1);
            
            if (choice == 1) {
                printf("Name : %s\nAge : %d\nBalance : %.2f\n", pUser->name, pUser->age, pUser->balance);
                break;   
            }
            
            printf("Ur balance is : %.2f", pUser->balance);
            break;

        case 3 :

            update(&user1);
            break;

        case 4:
            
            pUser = deposit(&user1);
            
            printf("Ur new balance is : %.2f", pUser->balance);

            break;

        case 5:

            pUser = withdraw(&user1);
            
            printf("Ur new balance is : %.2f", pUser->balance);

            break;

        case 6 : 
            is_Running = false;
            break;
        
        default:
            printf("Choice Invalid !");
            break;
        }
        

    }
    
    return 0;
}