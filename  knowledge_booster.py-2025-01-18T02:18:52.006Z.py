
import random
import requests
import json

# Define the topics and their corresponding API endpoints or data sources
topics = {
    "Science": "https://api.api-ninjas.com/v1/science",
    "Technology": "https://api.api-ninjas.com/v1/technology",
    "History": "https://api.api-ninjas.com/v1/history",
    "General Knowledge": "https://api.api-ninjas.com/v1/trivia"
}

# Function to fetch a random fact or concept from the selected topic
def get_random_fact(topic):
    api_endpoint = topics[topic]
    response = requests.get(api_endpoint, headers={'X-Api-Key': 'YOUR_API_KEY_HERE'})
    data = json.loads(response.text)
    return data[0]

# Function to display the menu and get the user's topic selection
def display_menu():
    print("Welcome to the Knowledge Booster!")
    print("Please select a topic:")
    for topic in topics:
        print(f"- {topic}")
    selected_topic = input("Enter your choice: ")
    return selected_topic

# Function to run the interactive quiz
def run_quiz(topic):
    fact = get_random_fact(topic)
    print(f"\nFact about {topic}: {fact['fact']}")

    # Multiple-choice questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": 0
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": 2
        },
        {
            "question": "Who invented the telephone?",
            "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Benjamin Franklin"],
            "answer": 1
        }
    ]

    score = 0
    for question in questions:
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer - 1 == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"\nYour final score: {score}/{len(questions)}")

# Main function
def main():
    selected_topic = display_menu()
    run_quiz(selected_topic)

if __name__ == "__main__":
    main()
