
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or trivia from the API
def get_random_fact_or_trivia(topic):
    api_key = "YOUR_API_KEY_HERE"
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    return selected_topic

# Function to display a random fact or trivia and quiz the user
def learn_and_quiz(topic):
    data = get_random_fact_or_trivia(topic)
    print(f"\nHere's a random {topic.lower()} fact or trivia:")
    if topic == "General Knowledge":
        print(data["question"])
        answers = data["options"]
        correct_answer = data["answer"]
    else:
        print(data["fact"])
        answers = ["True", "False"]
        correct_answer = "True"
    
    user_answer = input("Enter your answer (True/False or A/B/C/D): ").strip().upper()
    if user_answer == correct_answer:
        print("Correct! You're a knowledge master.")
    else:
        print(f"Oops, the correct answer is {correct_answer}.")

# Main program loop
while True:
    selected_topic = display_menu()
    if selected_topic in topics:
        learn_and_quiz(selected_topic)
        continue_prompt = input("\nDo you want to learn about another topic? (y/n) ").lower()
        if continue_prompt != "y":
            break
    else:
        print("Invalid topic. Please try again.")
