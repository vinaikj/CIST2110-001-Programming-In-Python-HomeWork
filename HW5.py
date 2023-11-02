# HW5.py
# Author: Jayant Vinaik

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
foodList = ["pizza","burger","pasta","chicken","fries"]
print()
print("------------------------------------------------------------")
print("printing fav foods list")
print("------------------------------------------------------------")
print(foodList)

# Question 2: Using the list from question 1, print the first and last element of the list
print()
print("------------------------------------------------------------")
print("Printing first and last elements")
print("------------------------------------------------------------")
print("first: ", foodList[0], "   last: ",foodList[-1])

# Question 3: Using the list from question 1, print the 3rd element of the list
print()
print("------------------------------------------------------------")
print("Printing third element")
print("------------------------------------------------------------")
print("3rd element: ", foodList[2])

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print()
print("------------------------------------------------------------")
print("Printing 1st through 3rd elements")
print("------------------------------------------------------------")
print("1st through 3rd elements: ", foodList[0:3])

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print()
print("------------------------------------------------------------")
print("Printing last 2 elements")
print("------------------------------------------------------------")
print("last 2 elements: ", foodList[-2:])

# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
print()
print("------------------------------------------------------------")
print("Printing foods in list")
print("------------------------------------------------------------")
for food in foodList:
    print(food)
  
# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
print()
print("------------------------------------------------------------")
print("Printing foods in reverse order")
print("------------------------------------------------------------")
for food in foodList[::-1]:
  print(food)

# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
print()
print("------------------------------------------------------------")
print("Printing list with index")
print("------------------------------------------------------------")
for i, food in enumerate(foodList):
  print(i, food)
  

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1,2,3],[4,5,6],[7,8,9]]
print()
print("------------------------------------------------------------")
print("Printing 1st element of second list")
print("------------------------------------------------------------")
print("First element of second list: ", list[1][0])


# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
def reverseList(list):
  return list[::-1]  


def main():
  print()
  print("------------------------------------------------------------")
  print("Calling reverse list function ")
  print("------------------------------------------------------------")
  print(reverseList(foodList))


if __name__ == "__main__":
  main()
