from random import randint
from time import sleep
import models.user as user
import utils.utilities as utilities


def pause(timer)  -> None:
    print(f"U have been paused for {timer} second")
    sleep(timer)

def set_valid_code() -> int:
    validate_code = randint(1000, 9999)
    return validate_code

def validator() -> bool:

    valid_code = set_valid_code()
    counter = 5

    while True:
        print(valid_code)
        if counter > 0:
            try :
                user_code = int(input(" => Code : "))
                if user_code == valid_code:
                    return True
                else :
                    counter -= 1
                    print(f"Wrong Code, u have {counter} try left")
            except ValueError:
                print(utilities.invalid_num())
        else:
            pause(20)
            valid_code = set_valid_code()
            counter = 5



def authenticate_user(users, entered_name : str, choice : int)  -> None:
    current_user = user.User.find_user(users, entered_name)

    if current_user is None:
        print("User not found")
    else:
        print(current_user.login())
        choice(current_user)