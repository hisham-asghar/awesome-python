Here is the raw Python code extracted from the JSON:

import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the API
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data[0]

# Function to display the menu and get the user's topic choice
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    return input("Enter your choice: ")

# Function to run the quiz for the selected topic
def run_quiz(topic):
    fact = get_random_fact(topic)
    print(f"\nHere's a {topic.lower()} fact for you:")
    print(fact["fact"])

    # Multiple-choice questions
    questions = [
        {
            "question": fact["question"],
            "choices": fact["choices"],
            "answer": fact["answer"]
        }
    ]

    # Ask the user the multiple-choice question
    score = 0
    for question in questions:
        print("\nQuestion:", question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i+1}. {choice}")
        user_answer = int(input("Enter your answer (1-4): "))
        if question["choices"][user_answer-1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    print(f"\nYour score: {score}/{len(questions)}")

# Main program loop
while True:
    topic = display_menu()
    run_quiz(topic)
    if input("Do you want to try another topic? (y/n) ").lower() != "y":
        break

print("Thank you for using the Interactive Knowledge Booster!")