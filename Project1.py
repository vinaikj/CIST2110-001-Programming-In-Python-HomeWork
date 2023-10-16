# Project1.py
# Author: Jayant Vinaik



#farewell message
def farewell(score): 
    print("Thank you for playing!")
    print("Your score is " + str(score) + " out of 7.") 

#welcome message
def Welcome(): 
    print("Welcome to the quiz game!")  
    print("You will be asked a series of questions.")
    print("There are 7 questiongs each will have 4 answer options (a, b, c, d).")
    print("Enter quit to end the game and exit")

#Ask question function  
def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
    print(question)
    print("a. " + option_1)
    print("b. " + option_2)
    print("c. " + option_3)
    print("d. " + option_4)
    user_answer = str(input("Enter your answer: "))
    if(user_answer == correct_answer):
        print("Correct!")   
        return True
    elif(user_answer == "a" or user_answer == "b" or user_answer == "c" or user_answer == "d"): 
        print("Incorrect!")
        return False   
    elif (user_answer == "quit"):
        print("Thank you for playing!")
        exit()
    else: 
        print("Invalid input, enter correct answer")
        ask_question(question, option_1, option_2, option_3, option_4, correct_answer) 

#main function 
def main():
    score = 0

    Welcome()

    if(ask_question("Question 1: What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", "b")):    
        score += 1  
    if(ask_question("Question 2: What is the national dish of India?", "Pizza", "Chicken Tikka", "Khichdi", "French Fries", "c")):     
        score += 1
    if(ask_question("Question 3: What is the official language of India?", "No offical language", "Hindi", "French", "Hindi", "b")):     
        score += 1  
    if(ask_question("Question 4: What is the name of Indian Prime Minister?", "Obama", "Narendra Modi", "Sadhguru", "Tom Brady", "b")):
        score += 1
    if(ask_question("Question 5: What is the festival of lights called?", "Diwali", "Holi", "Ramadan", "Christmas", "a")):
        score += 1  
    if(ask_question("Question 6: What is the popular form of music and dance from Punjab?", "Bhangra", "Raga", "Sattriya", "Tap dancing", "a")):
        score += 1  
    if(ask_question("Question 7: What is the capital of Japan?", "Tokyo", "Osaka", "Kyoto", "Yokohama", "a")):
        score += 1  
    if(ask_question("Question 8: What is the capital of Russia?", "Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "a")):
        score += 1  



    farewell(score)

if __name__ == "__main__":
    main()  
