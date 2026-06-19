from colorama import Fore, Style, init
init(autoreset=True)

def show_output(step: dict):
    for i, num in enumerate(step["array"]):
        if i in step["compare"] and step["swap"] == True:
            print(Fore.RED + str(num) + Style.RESET_ALL, end=" ")
        else:
            print(Fore.GREEN + str(num), end=" ")

def convert_input(number_input: str):  #TODO: Convert user's input to the right format
    formatted_input = [] 
    while True: 
        if number_input.isdigit():
            for num in number_input: < #Problem
                formatted_input.append(int(num))
            break
        else:
            number_input = input("Input numbers! ").strip()
    return formatted_input
#Suppose: number_input = 432 87
#Problem: What if the user want to add Ten(10)?