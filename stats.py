import time
from colorama import Fore, Style, init
from sorts import *
init(autoreset=True)

#inputting
def user_chose_bubble(sort_input: str):
    if sort_input == "1":
        return True
    else:
        return False

def show_bubble(lst: list):
    for step in bubble_sort(lst):
        show_output(step)
        time.sleep(0.6)

def show_output(step: dict):
    for i, num in enumerate(step["array"]):
        if i in step["compare"] and step["color"] == "red":
            print(Fore.RED + str(num) + Style.RESET_ALL, end=" ")
        elif i in step["compare"] and step["color"] == "cyan":
            print(Fore.CYAN + str(num) + Style.RESET_ALL, end=" ")
        elif i in step["bubbled"]:
            print(Fore.GREEN + str(num) + Style.RESET_ALL, end=" ") 
        else:
            print(str(num), end=" ")
    print("\n")


def convert_input(number_input: str):  #TODO: Convert user's input to the right format
    formatted_input = [] 
    while True: 
        if number_input.isdigit():
            for num in number_input:  #Problem
                formatted_input.append(int(num))
            break
        else:
            number_input = input("Input numbers! ").strip()
    return formatted_input
#Suppose: number_input = 432 87
#Problem: What if the user want to add Ten(10)?
#TODO: Let's focus on making it work first, then we can give users the freedom to input their own 

lst = [4, 5, 2, 1, 7, 3, 6]
show_bubble(lst)



