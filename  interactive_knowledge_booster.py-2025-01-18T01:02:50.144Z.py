
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").capitalize()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the chosen topic
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    
    # Randomly select a fact or concept from the data
    fact = random.choice(data)
    return fact

# Function to display the fact or concept and run the quiz
def run_quiz(topic, fact):
    print(f"\nHere's a random {topic.lower()} fact or concept:")
    print(fact["description"])
    
    # Prepare the multiple-choice questions
    questions = fact["questions"]
    
    # Run the quiz
    score = 0
    for question in questions:
        print(f"\n{question['question']}")
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid answer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["options"][question["answer"]-1])
    
    print(f"\nYour final score: {score}/{len(questions)}")

# Main function to run the program
def main():
    topic = display_menu()
    fact = get_random_fact(topic)
    run_quiz(topic, fact)

if __name__ == "__main__":
    main()
