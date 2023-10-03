# HW2.py
# Author: Jayant Vinaik


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:


# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

age= float(input("Enter your age: "))
if age < 13:
    print("You are a child.")   
elif age >= 13 and age <= 19:   
    print("You are a teenager.")            
elif age >= 20:
    print("You are an adult.")


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

temp = ""
for x in range(1,6):
    temp = temp + str(x)
    print(temp) 

# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.

numbers = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
 numbers[x] = int(input("Enter number "+ str(x+1) + ": "))  

print("The highest number is " + str(max(numbers))) 
print("The lowest number is " + str(min(numbers)))      
print("The average of all the numbers is " + str(sum(numbers)/len(numbers)))    



# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

userEnter = str(input("Enter a string: "))
userEnter.lower()

counter = 0
for x in userEnter:
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        counter = counter + 1           
print("The number of vowels in the string is " + str(counter))  