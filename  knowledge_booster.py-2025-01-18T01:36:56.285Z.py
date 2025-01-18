
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
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = topics[topic]
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        fact = response.json()["fact"]
        return fact
    else:
        return "Error fetching fact."

# Function to display the menu and get user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ").strip()
    if selected_topic in topics:
        return selected_topic
    else:
        print("Invalid topic. Please try again.")
        return None

# Function to run the interactive quiz
def run_quiz(topic):
    # Define quiz questions and answers for the selected topic
    quiz_data = {
        "Science": [
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Cu", "Fe"],
                "answer": "Au"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Jupiter"
            }
        ],
        "Technology": [
            {
                "question": "What is the primary function of a computer's CPU?",
                "options": ["Storage", "Input/Output", "Processing", "Memory"],
                "answer": "Processing"
            },
            {
                "question": "What is the name of the first programmable computer?",
                "options": ["ENIAC", "UNIVAC", "Z1", "MARK I"],
                "answer": "ENIAC"
            }
        ],
        "History": [
            {
                "question": "In what year did World War II end?",
                "options": ["1945", "1939", "1941", "1947"],
                "answer": "1945"
            },
            {
                "question": "Who was the first president of the United States?",
                "options": ["Abraham Lincoln", "Thomas Jefferson", "George Washington", "John Adams"],
                "answer": "George Washington"
            }
        ],
        "General Knowledge": [
            {
                "question": "What is the capital city of Australia?",
                "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
                "answer": "Canberra"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", "Indian Ocean"],
                "answer": "Pacific Ocean"
            }
        ]
    }

    # Run the quiz
    score = 0
    for question in quiz_data[topic]:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer (1-4): ")
        if user_answer.strip() == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])
    print(f"Your final score: {score}/{len(quiz_data[topic])}")

# Main program loop
while True:
    selected_topic = display_menu()
    if selected_topic:
        random_fact = get_random_fact(selected_topic)
        print(f"\nRandom {selected_topic} fact: {random_fact}")
        run_quiz(selected_topic)
        print("\nThank you for using the Knowledge Booster!")
        break
