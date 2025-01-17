Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = topics[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

# Function to display the random fact or concept
def display_fact(fact):
    print(f"Did you know that {fact['description']}?")

# Function to display the quiz and get the user's answer
def display_quiz(topic):
    url = topics[topic] + "/quiz"
    response = requests.get(url)
    quiz_data = response.json()
    
    question = quiz_data["question"]
    options = quiz_data["options"]
    correct_answer = quiz_data["correct_answer"]
    
    print(f"Question: {question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    while True:
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            if options[int(user_answer) - 1] == correct_answer:
                print("Correct!")
                return
            else:
                print("Incorrect. Please try again.")
        else:
            print("Invalid input. Please try again.")

# Main function to run the knowledge booster
def run_knowledge_booster():
    topic = display_menu()
    fact = get_random_fact(topic)
    display_fact(fact)
    display_quiz(topic)

run_knowledge_booster()
