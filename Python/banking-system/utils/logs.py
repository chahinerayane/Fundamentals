#-------------------------------#
#                               #
#             LOGS              #
#                               #
#-------------------------------#

from datetime import datetime


def current_time() -> str:
    now = datetime.now()
    formatted_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_string


def write_log(filename, message):
    with open(filename, "a", encoding="utf-8") as logs_file:
        logs_file.write(message)

def login_logs(current_user) -> None:
    write_log("logs/login_logs.txt", f"[{current_time()}] {current_user} logged in \n")


def deposit_logs(current_user, amount, newbalance):
    write_log("logs/deposit_logs.txt", f"[{current_time()}] {current_user} deposited {amount} new balance is : {newbalance} \n")


def withdraw_logs(current_user, amount, newbalance):
    write_log("logs/withdraw_logs.txt", f"[{current_time()}] {current_user} withdrew : {amount} new balance is : {newbalance} \n")

def edit_country_logs(current_user, oldcountry ,newcountry) :    
    write_log("logs/edit_country_logs.txt", f"[{current_time()}] {current_user} \ncountry changed from {oldcountry} to {newcountry} \n")

def edit_username_logs(current_user, newname) :    
    write_log("logs/edit_username_logs.txt", f"[{current_time()}] {current_user} changed name to {newname} \n")

def edit_transfer_logs(current_user, recipient, amount) :    
    write_log("logs/edit_transfer_logs.txt", f"[{current_time()}] {current_user} transferred {amount} to {recipient} \n")

def logout_logs(current_user):
    write_log("logs/logout_logs.txt", f"[{current_time()}] {current_user} disconnected \n")