
import random
import requests
import json

# Define the available topics
topics = {
    "1": "Science",
    "2": "Technology",
    "3": "History",
    "4": "General Knowledge"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for key, value in topics.items():
        print(f"{key}. {value}")
    return input("Enter your choice (1-4): ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = f"https://api.example.com/facts/{topic.lower()}"
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

# Function to display the random fact or concept
def display_fact(fact):
    print(f"Did you know? {fact}")

# Function to create a multiple-choice quiz
def quiz(topic):
    url = f"https://api.example.com/quiz/{topic.lower()}"
    response = requests.get(url)
    data = response.json()
    
    correct_answers = 0
    for question in data:
        print(question["question"])
        choices = question["choices"]
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question["answer"]:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect. The correct answer is:", choices[question["answer"]-1])
    
    print(f"You got {correct_answers} out of {len(data)} questions correct.")

# Main function to run the program
def main():
    user_choice = display_menu()
    topic = topics[user_choice]
    
    fact = get_random_fact(topic)
    display_fact(fact)
    
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)

if __name__ == "__main__":
    main()
