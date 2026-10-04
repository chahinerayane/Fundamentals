from pyfiglet import figlet_format
from termcolor import colored
from os import system
from time import sleep

def cmd_cleaner(delay=0) :
    sleep(delay)
    system("cls")

def logo(title) -> str:
    return colored(figlet_format(title), "blue")

def database_err(err : str) -> None:
    print(f"Database error {err}")

def resume(delay):
    cmd_cleaner(delay)
    print(logo("TO DO LIST"))


def todo_not_exists(cr, name):
    cr.execute("SELECT * FROM todo WHERE name = ?", (name,))

    return cr.fetchone() is None