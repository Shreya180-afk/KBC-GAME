# creating a python program that displays the questions to the user like kbc
# KBC is a television program in which the host Amitabh Bachan asked questions to the contestant and if th eanswer is write he/she will awarded with th emoney but if the answer is wrong then he/she will out from the game 
# for this we are going to use list data type to store th equestions and their correct answers
#  display the final amount the user is taking to the after finishing the game
# 
questions = [
    ["1. What is the correct way to declare a variable in Python?", "a) int x = 10", "b) var x = 10", "c) x = 10", "d) declare x = 10", 3],
    ["2. Which of the following is a valid keyword in Python?", "a) switch", "b) constant", "c) class", "d) goto", 2],
    ["3. What is the output of the following code? print(2 * 3 + 5)", "a) 16", "b) 11", "c) 21", "d) 10", 1],
    ["4. In C, what is the size of the int data type typically?", "a) 2 bytes", "b) 4 bytes", "c) 8 bytes", "d) 16 bytes", 2],
    ["5. Which of the following languages is used for developing iOS apps?", "a) Java", "b) Swift", "c) Python", "d) C#", 2],
    ["6. In Java, what is the output of the following code? System.out.println(10 / 3);", "a) 3", "b) 3.33", "c) 3.0", "d) 1", 3],
    ["7. What is the function of super() in object-oriented programming (OOP)?", "a) Creates a new class", "b) Calls the parent class constructor", "c) Initializes the object", "d) Terminates the class", 2],
    ["8. Which of the following data structures follows the Last-In-First-Out (LIFO) principle?", "a) Queue", "b) Stack", "c) Array", "d) Linked List", 2],
    ["9. What does the term recursion refer to in programming?", "a) A function that calls another function", "b) A function that calls itself", "c) An infinite loop", "d) A repeated condition", 2],
    ["10. In SQL, which command is used to retrieve data from a database?", "a) SELECT", "b) UPDATE", "c) INSERT", "d) DELETE", 1]
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 25000, 50000, 75000, 100000]

for i in range(len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"{question[1]}    {question[2]}")
    print(f"{question[3]}    {question[4]}")
    
    reply = int(input("Enter your answer (1-4) or 0 to Quit: "))
    if (reply == 0):
        money = levels[i-1]
        break
    # Convert the index to the correct option letter
    correct_answer_index = question[-1]
    
    if reply == correct_answer_index:
        print(f"Correct answer, you have won Rs.{levels[i]}")
        money = levels[i]
    else:
        print("Wrong Answer")
        break
print(f"Total Winning money {money}")
