from stats import *
from sorts import *
user_input = input("1. Visualize Sorts\n2. EXIT")
if user_input == "1":
    sort_input = input("1. Bubble Sort\n Selection Sort\n Insertion Sort")
    number_input = input("Numbers to sort: ").strip()
    if sort_input == "1":
        for array in bubble_sort(number_input):
            show_output(array)


lst = [4, 7, 2, 5, 3, 1, 6]


