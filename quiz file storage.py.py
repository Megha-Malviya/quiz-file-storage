import random  

def read_questions_from_file(filename):  
    questions = []  
    try:  
        with open(filename, 'r') as file:  
            for line in file:   
                parts = line.strip().rsplit(',', 1)   
                if len(parts) == 2:  
                    question, answer = parts  
                    question = question.strip()  
                    answer = answer.strip().upper()    
                    questions.append((question, answer))  
    except FileNotFoundError:  
        print(f"Error: The file {filename} was not found.")  
    return questions  

 

questions_dbms = read_questions_from_file('questions_dbms.txt')  
questions_python = read_questions_from_file('questions_python.txt')  
questions_java = read_questions_from_file('questions_java.txt')  

print(f"Python questions loaded: {len(questions_python)}")  
print(f"DBMS questions loaded: {len(questions_dbms)}")  
print(f"Java questions loaded: {len(questions_java)}")

accounts = {}  

def register():  
    username = input("Create a username: ")  
    if username in accounts:  
        print("Username already exists. Try again.")  
        return False  
    password = input("Create a password: ")  
    accounts[username] = password  
    print("Registration successful!")  
    return True  

def login():  
    username = input("Enter your username: ")  
    if username not in accounts:  
        print("Username does not exist.")  
        return False  
    password = input("Enter your password: ")  
    if accounts[username] != password:  
        print("Incorrect password.")  
        return False  
    print("Login successful!")  
    return True  

def select_quiz():  
    print("\nSelect a quiz:")  
    print("1. Python")  
    print("2. DBMS")  
    print("3. Java")  
    choice = input("Enter the choice number (1-3): ")  
    if choice == '1':  
        if len(questions_python) < 5:  
            print("Not enough questions available for Python quiz.")  
            return None  
        return random.sample(questions_python, 5)  
    elif choice == '2':  
        if len(questions_dbms) < 5:  
            print("Not enough questions available for DBMS quiz.")  
            return None  
        return random.sample(questions_dbms, 5)  
    elif choice == '3':  
        if len(questions_java) < 5:  
            print("Not enough questions available for Java quiz.")  
            return None  
        return random.sample(questions_java, 5)  
    else:  
        print("Invalid choice. Exiting.")  
        return None  

def take_quiz(questions):  
    score = 0  
    for question, answer in questions:  
        user_answer = input(f"{question} ")  
        if user_answer.strip().upper() == answer:  
            score += 1  
            print("Correct!")  
        else:  
            print(f"Wrong! The correct answer is: {answer}")  
    return score  

def main():  
    while True:  
        print("\nWelcome to the Quiz Application!")  
        print("1. Register")  
        print("2. Login")  
        print("3. Exit")  
        action = input("Select an option (1-3): ")  

        if action == '1':  
            register()  
        elif action == '2':  
            if login():  
                questions = select_quiz()  
                if questions:  
                    score = take_quiz(questions)  
                    print(f"You got {score} out of 5 correct!")  
            else:  
                print("Login failed.")  
        elif action == '3':  
            print("Thank you for using the Quiz Application!")  
            break  
        else:  
            print("Invalid option. Please try again.")  

if __name__ == "__main__":  
    main()
