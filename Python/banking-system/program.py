import utils.validator as validator
import models.user as user
import utils.utilities as utilities


users = [
    user.Customer("Jahanam", "Morocco", 250000),
    user.Customer("Sara", "France", 2000),
]


def edit_profile(current_user : user.User) -> None:
    edit_choices = {
        1 : "EDIT USERNAME",
        2 : "EDIT COUNTRY"
    }
    while True :
        utilities.cmd_cleaner()
        print(utilities.logo("JahanamV2", "red"))
        for edit_choice_key,edit_choice_value in edit_choices.items():
            print(f"{edit_choice_key} : {edit_choice_value.capitalize()}")
        try : 
            entered_choice = int(input(" => "))
            if entered_choice in edit_choices:
                if entered_choice == 1 :
                    new_name = input("Enter your new username:")
                    current_user.set_name(new_name)
                    print(current_user.get_all_info())
                    utilities.cmd_cleaner(2)
                    break
                elif entered_choice == 2:
                    new_country = input("Enter your new Country : ")
                    current_user.set_country(new_country)
                    print(current_user.get_all_info())
                    utilities.cmd_cleaner(2)
                    break
            else :
                print("choice not found !")
        except ValueError:
            print("Invalid choice")
        

def profile_menu(current_user) -> None:
    print(current_user.get_all_info())
    input("Press enter to return........!")

def validate() -> bool:
    utilities.cmd_cleaner()
    print(utilities.logo("VALIDATOR", "green"))
    return validator.validator()


def deposit_menu(current_user) -> None:
    while True:
        try :
            amount = int(input("Enter the amount to add : "))
            if amount > 0:
                    utilities.cmd_cleaner()
                    if validate():
                        print(f" => Your new balance is : {current_user.deposit(amount)}")
                        utilities.cmd_cleaner(1.9)
                        print(utilities.logo("JahanamV2", "red"))
                        return
            else :
                print(utilities.valid_num())
        except ValueError:
            print(utilities.invalid_num())
    
    
def withdraw_menu(current_user) -> None:
    while True:
        try :
            amount = int(input("Enter the amount to withdraw : "))
            if amount > 0:
                    utilities.cmd_cleaner()
                    if validate():
                        result = current_user.withdraw(amount)
                        if result["success"]:
                            print(f"Withdrawal successful!")
                            print(f"New balance: {result['balance']}")
                            utilities.cmd_cleaner(1.9)
                            print(utilities.logo("JahanamV2", "red"))
                            return
                        else:
                            print(result["message"])
            else :
                print(utilities.valid_num())
        except ValueError:
            print(utilities.invalid_num())



def transfer_menu(current_user, users) -> None:
    receiver_name = input(" => receiver username : ")
    recipient = user.User.find_user(users, receiver_name)
    if recipient is None:
        print("User not found")
    else:
        if recipient != current_user:
            try :
                amount = int(input(f"Enter the amount to send to {recipient.get_name()} : "))
                result = current_user.transfer(recipient, amount)

                if validate():
                    if result["success"]:
                        print(f"Transfer successful!")
                        print(f"New balance: {result['balance']}")
                    else:
                        print(result["message"])

            except ValueError:
                print(utilities.invalid_num())
        else :
            print("You can not enter your own name")


def choice(current_user) -> None:
    label_menu = {
        1: "Profile",
        2: "Deposit",
        3: "Withdraw",
        4: "Transfer",
        5: "Edit Profile",
        6: "Logout",
    }
    actions = {
        1: lambda: profile_menu(current_user),
        2: lambda: deposit_menu(current_user),
        3: lambda: withdraw_menu(current_user),
        4: lambda: transfer_menu(current_user, users),
        5: lambda: edit_profile(current_user),
        6: lambda: current_user.disconnect(),
    }
    while True:
        utilities.cmd_cleaner()
        print(utilities.logo("JahanamV2", "red"))
        for choice_key, choice_value in label_menu.items():
            print(f"{choice_key} : {choice_value.capitalize()}")
        try :
            input_choice = int(input("\n => Enter your choice number : "))
            if input_choice in actions:
                actions[input_choice]()

                if input_choice == 4:
                    utilities.cmd_cleaner(0.9)

                if input_choice == 6:
                    return

            else :
                print("Invalid choice.")
                utilities.cmd_cleaner(0.9)
        except ValueError :
            print(utilities.valid_num())


utilities.cmd_cleaner(0.2)
print(utilities.logo("JahanamV2", "red"))

# starting here

entered_name = input("Enter your username : ")


validator.authenticate_user(users, entered_name, choice)




    

