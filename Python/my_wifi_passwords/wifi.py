import os 
import time


class Wifi:
    def CmdCleaner():
        os.system("cls")
    def GetWifinames():
        os.system("netsh wlan show profile")
    def PassGetter(name):
        os.system(f'netsh wlan show profile "{name}" key=clear')

try:
    choice = int(input("Enter 1 to start: "))
except ValueError:
    print("Please enter a number.")



if choice == 1:
    Wifi.CmdCleaner()
    Wifi.GetWifinames()
    name = input("enter the name of the wifi u want : ")
    Wifi.CmdCleaner()
    time.sleep(1.4)
    Wifi.PassGetter(name)
