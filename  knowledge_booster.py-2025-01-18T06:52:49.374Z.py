
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "science": "https://api.api-ninjas.com/v1/science",
    "technology": "https://api.api-ninjas.com/v1/technology",
    "history": "https://api.api-ninjas.com/v1/history",
    "general_knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"{topic.capitalize()}")
    user_input = input("Enter your choice: ").lower()
    return user_input

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    print(f"\nHere's a {topic.capitalize()} fact for you:")
    print(fact["fact"])

    # Multiple-choice questions
    questions = [
        {
            "question": fact["question"],
            "options": fact["options"],
            "answer": fact["answer"]
        }
    ]

    for question in questions:
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question['answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")

# Main program loop
while True:
    topic = display_menu()
    if topic in topics:
        run_quiz(topic)
    else:
        print("Invalid topic. Please try again.")
    continue_input = input("\nDo you want to try another topic? (y/n) ").lower()
    if continue_input != "y":
        break

print("\nThank you for using the Knowledge Booster. Have a great day!")
