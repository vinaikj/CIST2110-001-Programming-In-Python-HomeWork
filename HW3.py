# HW3.py
# Author:Jayant vinaik  

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

import random
import math
import sys as system
import os

def square_number(number):
    return number ** 2

def replace_char_at_index(input_string, replacement_char, index):
    if index < 0 or index >= len(input_string):
        return input_string  # Index out of range, return the original string unchanged
    else:
        return input_string[:index] + replacement_char + input_string[index + 1:]

def is_within_bounds(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

def get_user_info():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    color = input("Please enter your favorite color: ")
    return name, age, color

def print_user_info(name, age, color):
    print(f"Hello, my name is {name}. I am {str(age)} years old. My favorite color is {color}.")

def generate_random():
    random_number = random.randint(1, 100)
    print

def find_square_root(number):
    square_root = math.sqrt(number)
    print("The square root of " + str(number) + " = " + str(square_root))


def display_version():
    python_version = system.version
    print("Python Version:", python_version)


def display_cwd():
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)

def main():
    # Your main logic goes here
   print (square_number(16)  )  
   print(replace_char_at_index("Good Evening", "!", 2)  ) 
   print(is_within_bounds(5, 1, 10)  ) 
   get_user_info() 
   print_user_info("Jayant", 21, "Blue")   
   generate_random()   
   find_square_root(16)   
   display_version()    
   display_cwd()   

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()