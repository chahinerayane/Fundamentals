#-------------------------------#
#                               #
#             USER              #
#                               #
#-------------------------------#

import utils.logs as logs


class User:

    
    def __init__(self, username, country, bank=0):
        self.__username = username
        self.__country  = country
        self.__bank = bank


    def login(self) -> str:
        logs.login_logs(self.__username) 
        return f"Logged as {self.__username}"


    def deposit(self, amount : int) -> int:
        self.__bank += amount
        logs.deposit_logs(self.__username, amount, self.__bank)
        return self.__bank


    def withdraw(self, amount : int) -> int:
        if self.__bank >= amount:
            self.__bank -= amount
            logs.withdraw_logs(self.__username, amount, self.__bank)
            return {
                "success": True,
                "balance": self.__bank
            }
        else :
            return {
                "success": False,
                "message": "Not enough balance"
            }


    def transfer(self, recipient : str, amount : int):
        if self.__bank >= amount:
            self.__bank -= amount
            recipient.__bank += amount
            logs.edit_transfer_logs(self.__username, recipient.get_name(), amount)
            return {
                "success": True,
                "balance": self.__bank
            }
        else :
            return {
                "success": False,
                "message": "Not enough balance"
            }
    
    def get_name(self):
        return self.__username

    def set_name(self, newname : str) -> str:
        logs.edit_username_logs(self.__username, newname)
        self.__username = newname

    def set_country(self, newcountry : str) -> str:
        logs.edit_country_logs(self.__username, self.__country, newcountry)
        self.__country = newcountry
    
    def get_all_info(self) -> str:
        return f"""
        ===================== INFO =====================
        => Username : {self.__username}
        => country  : {self.__country}
        => bank     : {self.__bank}
        ================================================
        """
    
    
    @staticmethod
    def find_user(users, search_username):
        for current_user in users:
            if current_user.get_name().lower() == search_username.strip().lower():
                return current_user
        return None


    def disconnect(self):
        logs.logout_logs(self.__username)

class Customer(User):
    def __init__(self, username, country, bank=0):
        super().__init__(username, country, bank)

    


