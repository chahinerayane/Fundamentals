from random import choice,shuffle
from string import ascii_lowercase, ascii_uppercase, punctuation



numbers_list = "1234567890"
lowercase_list = ascii_lowercase
uppercase_list = ascii_uppercase
specialchar_list = punctuation

def add_required_characters():

    password = ""

    password += choice(numbers_list)
    password += choice(lowercase_list)
    password += choice(uppercase_list)
    password += choice(specialchar_list)

    return password


def shuffle_password(password):

    chars = list(password)
    shuffle(chars)
    password = "".join(chars)


    return password

def generate_password(length):
    password = add_required_characters()

    all_list = [numbers_list, lowercase_list, uppercase_list, specialchar_list]

    for i in range(length - 4):
        choosen_list = choice(all_list)

        password += choice(choosen_list)

    password = shuffle_password(password)


    return password


while True:
    try : 
        length = int(input("Enter the password length : ").strip())
        if length > 3:
            break
        else :
            print("Password length must be greater than 3.")
    except ValueError:
        print("Enter valid number.")


print(generate_password(length))





