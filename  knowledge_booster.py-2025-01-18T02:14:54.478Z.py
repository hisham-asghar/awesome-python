Here is the raw Python code extracted from the JSON:

```python
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
TOPICS = {
    "Science": "https://api.example.com/science",
    "Technology": "https://api.example.com/technology",
    "History": "https://api.example.com/history",
    "General Knowledge": "https://api.example.com/general-knowledge"
}

# Function to display the menu and get user's choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in TOPICS:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    url = TOPICS[topic]
    response = requests.get(url)
    data = response.json()
    return random.choice(data)

# Function to display the random fact or concept
def display_fact(fact):
    print(f"Did you know? {fact}")

# Function to create a multiple-choice quiz for the selected topic
def create_quiz(topic):
    url = TOPICS[topic]
    response = requests.get(url)
    data = response.json()
    question = random.choice(data)
    choices = [question["answer"]] + [random.choice(data)["answer"] for _ in range(3)]
    random.shuffle(choices)
    print(f"Question: {question['question']}")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = int(input("Enter your answer (1-4): "))
    return user_answer == choices.index(question["answer"]) + 1

# Main function to run the interactive knowledge booster
def run_knowledge_booster():
    topic = display_menu()
    fact = get_random_fact(topic)
    display_fact(fact)
    if create_quiz(topic):
        print("Correct! You've increased your knowledge.")
    else:
        print("Oops, that's not the right answer. Better luck next time!")

# Run the knowledge booster
run_knowledge_booster()
