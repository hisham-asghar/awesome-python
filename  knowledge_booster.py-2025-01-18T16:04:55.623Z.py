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
    "General Knowledge": "https://api.example.com/general_knowledge"
}

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    # Use the appropriate API or data source to fetch a random fact or concept
    response = requests.get(topics[topic])
    data = response.json()
    return random.choice(data)

# Function to display the random fact or concept
def display_fact(fact):
    print(f"Did you know? {fact}")

# Function to create a multiple-choice quiz for the selected topic
def create_quiz(topic):
    # Use the appropriate API or data source to fetch quiz questions and answers
    response = requests.get(topics[topic] + "/quiz")
    quiz_data = response.json()

    # Select a random question and its choices
    question = random.choice(quiz_data["questions"])
    choices = question["choices"]
    random.shuffle(choices)

    # Display the question and choices
    print(f"Question: {question['question']}")
    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice}")

    # Get the user's answer
    user_answer = int(input("Enter your answer (1-4): "))
    if choices[user_answer - 1] == question["answer"]:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question['answer']}")

# Main function to run the knowledge booster
def run_knowledge_booster():
    topic = display_menu()
    fact = get_random_fact(topic)
    display_fact(fact)
    create_quiz(topic)

if __name__ == "__main__":
    run_knowledge_booster()
