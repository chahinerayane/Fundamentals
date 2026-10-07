from pyfiglet import figlet_format
from termcolor import colored
from string import punctuation



def logo(name,color):
    return colored(
        figlet_format(name),
        color = color,
    )

def icon(checked):
    return "✅" if checked else "❌"

def length_checker(password):
    if len(password) >= 8 :
        return True
    else:
        return False

def is_12_chars_or_more(password):
    if len(password) >= 12:
        return True
    else:
        return False
    
def digit_checker(password):
    for i in password:
        if i.isdigit():
            return True
    else:
        return False

def special_characters(password):
    for i in password:
        if i in punctuation:
            return True
    else:
        return False

def lowercase(password):
    for i in password:
        if i.islower():
            return True
    else:
            return False

def uppercase(password):
    for i in password:
        if i.isupper():
            return True
    else:
        return False

def detect_spaces(password):
    if " " not in password:
        return True
    else:
        return False


def common_password(password):
    with open("pass.txt", "r", encoding="utf-8") as commonpasswords:
        commons = commonpasswords.readlines()
        for common in commons:
                common = common.strip("\n")
                if common == password:
                    return False
        else:
             return True

def all_password_checker(password):
    score = 0
    if length_checker(password):
        print(f"Length : {icon(True)}")
        score += 1
    else:
        print(f"Length : {icon(False)}")


    if digit_checker(password):
        print(f"Digit : {icon(True)}")
        score += 1
    else:
        print(f"Digit : {icon(False)}")


    if special_characters(password):
        print(f"Special characters : {icon(True)}")
        score += 1
    else:
        print(f"Special characters : {icon(False)}")

    if lowercase(password):
        print(f"Lowercase : {icon(True)}")
        score += 1
    else:
        print(f"Lowercase : {icon(False)}")

    if uppercase(password):
        print(f"Uppercase : {icon(True)}")
        score += 1
    else:
        print(f"Uppercase : {icon(False)}")

    if detect_spaces(password):
        print(f"No space : {icon(True)}")
        score += 1
    else:
        print(f"No space : {icon(False)}")

    if common_password(password):
        print(f"Not a Common Password : {icon(True)}")
        score += 1
    else:
        print(f"Not a Common Password : {icon(False)}")

    return score

def suggestions(password):
    all_checker_list = [length_checker(password), digit_checker(password), special_characters(password), lowercase(password), uppercase(password),detect_spaces(password),common_password(password)]
    if not all(all_checker_list) :
        print("\n", " SUGGESTIONS ".center(80,"#"))
        if not length_checker(password):
            print(" - Use at least 8 characters.")

        if not digit_checker(password):
            print(" - Add a digit.")

        if not special_characters(password):
            print(" - Add a special character.")

        if not lowercase(password):
            print(" - Add a lowercase letter.")

        if not uppercase(password):
            print(" - Add an uppercase letter.")

        if not detect_spaces(password):
            print(" - Remove spaces from the password.")

        if not common_password(password):
            print(" - Common password is detected ⚠️")

        print("#" * 80)


def scorechecker(score,password):
    print(f"Score = {score}/7")
    if score in [6,7]:
        if is_12_chars_or_more(password) :
            print("Strength : Strong")
        else:
            print("Add at least 12 characters for a Strong rating.")
    elif score in [3, 4, 5]:
        print("Strength : Medium")
    elif  score == 2:
        print("Strength : Weak") 
    else:
        print("Strength : Very Weak")

    suggestions(password)


print(logo("CHECKER","red"))

password = input("Enter your strong password : ").strip()
score = all_password_checker(password)
scorechecker(score,password)





