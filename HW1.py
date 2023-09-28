# HW1.py
# Author:Jayant vinaik

# Question 1:
# Print Hello World like we did in class

print("Hello World")

# Question 2:
# Print the following:
# Your name

print("Jayant Vinaik")

# Your age

print("20")

# Your favorite color

print("Purple")
# Your favorite animal

print("Elephant")
# Question 3:
# Create a variable called "myName" and set it equal to your name

myName = "Jayant Vinaik"


# Create a variable called "myAge" and set it equal to your age

myAge = "20"    


# Create a variable called "myColor" and set it equal to your favorite color

myColor = "Purple"

# Create a variable called "myAnimal" and set it equal to your favorite animal

myAnimal = "Elephant"

# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>

print("Hello, my name is " + myName  + "\n" + "I am " + myAge + " years old" + "\n" + "My favorite color is " + myColor + "\n" + "My favorite animal is " + myAnimal)

# Question 4:
# Calculate the following and print the result:
# 2 + 2

print(2 + 2)


# 3 * 4

print(3 * 4)

print(5 - 6)

# 8 / 2
print(8 / 2)
      

# Question 5:
# Create a variable called "num1" and set it equal to 2

num1 = 2

# Create a variable called "num2" and set it equal to 3

num2 = 3

# Create a variable called "num3" and set it equal to 4

num3 = 4

# Create a variable called "num4" and set it equal to 5

num4 = 5

# Calculate the following and print the result:
# num1 + num2
print(num1 + num2)

# num3 * num4
print(num3 * num4)

# num4 - num1

print(num4 - num1)
# num2 / num1

print(num2 / num1)
# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers.

user_name = input("Please enter your name: ")

print

# The program should then ask the user for three numbers (floats) and print the following:

num1 = float(input("Please enter a number: "))  

num2 = float(input("Please enter a number: "))  

num3 = float(input("Please enter a number: "))  

# 1. The sum of the three numbers is <sum>

userSum = num1 + num2 + num3    

print("The sum of the three numbers is " + str(userSum))
  

# 2. The product of the three numbers is <product>

userProduct = num1 * num2 * num3 

print("The product of the three numbers is " + str(userProduct))


# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 

userRound = round(num1) + round(num2) + round(num3) / 3

print("The sum of the three rounded numbers is " + str(userRound))


# 4. The average of the three numbers is <average>

userAverage = (num1 + num2 + num3) / 3

print("The average of the three numbers is " + str(userAverage))

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.


userSymbol = input("Please enter a symbol: ")

print("#           " + userSymbol,   end="          |\n")
print("#          " + userSymbol*3, end="         |\n")
print("#         " + userSymbol*5, end="        |\n")
print("#        " + userSymbol*7, end="       |\n")
print("#         " + userSymbol*5, end="        |\n")
print("#          " + userSymbol*3, end="         |\n") 
print("#           " + userSymbol,   end="          |\n")

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
