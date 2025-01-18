
import random
import requests
import json

# Define topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/randomfact?category=science",
    "Technology": "https://api.api-ninjas.com/v1/randomfact?category=technology",
    "History": "https://api.api-ninjas.com/v1/randomfact?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/randomfact?category=general"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"
    headers = {'X-Api-Key': api_key}
    response = requests.get(topics[topic], headers=headers)
    if response.status_code == 200:
        fact = response.json()['fact']
        return fact
    else:
        return "Error fetching fact."

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Interactive Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    user_input = input("Enter your choice: ")
    if user_input in topics:
        return user_input
    else:
        print("Invalid choice. Please try again.")
        return display_menu()

# Function to run the interactive quiz
def run_quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    quiz_questions = [
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
            "answer": 0
        },
        {
            "question": "What is the capital city of France?",
            "options": ["London", "Paris", "Berlin", "Rome"],
            "answer": 1
        },
        {
            "question": "Who invented the telephone?",
            "options": ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Benjamin Franklin"],
            "answer": 0
        }
    ]

    score = 0
    for question in quiz_questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["options"][question["answer"]])
    print(f"Your final score is: {score}/{len(quiz_questions)}")

# Main program loop
while True:
    selected_topic = display_menu()
    random_fact = get_random_fact(selected_topic)
    print(f"\nHere's a random {selected_topic.lower()} fact:\n{random_fact}")
    print("\nNow, let's test your knowledge with a quiz!")
    run_quiz(selected_topic)
    play_again = input("\nDo you want to try another topic? (y/n) ")
    if play_again.lower() != "y":
        break

print("Thank you for using the Interactive Knowledge Booster. Have a great day!")
