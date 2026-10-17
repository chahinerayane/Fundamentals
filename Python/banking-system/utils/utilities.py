from os import system
from pyfiglet import figlet_format
from termcolor import colored
from time import sleep

def cmd_cleaner(delay=0) -> None:
        sleep(delay)
        system("cls")

def logo(name ,color : str) -> str : 
    return colored(figlet_format(name), color)

def invalid_num() -> str:
      return "Please enter a valid number."

def valid_num() -> str:
      return "Please enter a positive number."
            


