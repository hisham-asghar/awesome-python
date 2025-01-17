
import random
import requests
import json

# Define the topics and their corresponding API endpoints
topics = {
    "Science": "https://api.api-ninjas.com/v1/facts?category=science",
    "Technology": "https://api.api-ninjas.com/v1/facts?category=technology",
    "History": "https://api.api-ninjas.com/v1/facts?category=history",
    "General Knowledge": "https://api.api-ninjas.com/v1/facts?category=general"
}

# Function to display the menu and get user's topic choice
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    
    while True:
        choice = input("Enter your choice: ").capitalize()
        if choice in topics:
            return choice
        else:
            print("Invalid choice. Please try again.")

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        facts = response.json()
        random_fact = random.choice(facts)
        return random_fact["fact"]
    else:
        return "Failed to fetch a fact. Please try again later."

# Function to display the quiz and get user's answers
def quiz(topic):
    # Fetch quiz questions and answers from a predefined database or API
    quiz_data = {
        "Science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            # Add more quiz questions and answers for Science
        ],
        "Technology": [
            {
                "question": "What does CPU stand for?",
                "options": ["Central Processing Unit", "Computer Power Unit", "Computational Power Unit", "Central Power Unit"],
                "answer": "Central Processing Unit"
            },
            # Add more quiz questions and answers for Technology
        ],
        # Add more quiz data for History and General Knowledge
    }
    
    score = 0
    for question in quiz_data[topic]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        
        user_answer = input("Enter your answer (1-4): ")
        if question["options"][int(user_answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    
    print(f"Your final score is: {score}/{len(quiz_data[topic])}")

# Main program loop
while True:
    topic = display_menu()
    print("\nHere's a random fact about", topic.lower() + ":")
    print(get_random_fact(topic))
    print("\nNow, let's test your knowledge with a quiz!")
    quiz(topic)
    
    again = input("\nDo you want to explore another topic? (y/n) ").lower()
    if again != "y":
        print("Thank you for using the Knowledge Booster!")
        break
